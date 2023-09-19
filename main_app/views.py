import uuid
import boto3
import os
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, reverse
from .models import Restaurant, Day, Review
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Restaurant, Day, Photo, DAYS_OF_WEEK
from .forms import ReviewForm, DayForm
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

def restaurants_index(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/index.html', {
        'restaurants': restaurants
    })

def restaurants_detail(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    days = Day.objects.all()
    return render(request, 'restaurants/detail.html', {
        'restaurant': restaurant,
        'days': days
    })

class RestaurantCreate(LoginRequiredMixin, CreateView):
    model = Restaurant
    fields = ['name', 'address', 'city', 'state', 'zip_code', 'cuisine', 'dine_in', 'take_out', 'delivery', 'drive_thru']

    def form_valid(self, form):
        # Assign the logged-in user to the restaurant
        form.instance.user = self.request.user
        return super().form_valid(form)

class RestaurantUpdate(UpdateView):
    model = Restaurant
    fields = ['dine_in', 'take_out', 'delivery', 'drive_thru']

class RestaurantDelete(DeleteView):
    model = Restaurant
    success_url = '/restaurants'


class DayCreate(CreateView):
    model = Day
    fields = ['days', 'opening_time', 'closing_time']

class DayDetail(DetailView):
    model = Day

class DayUpdate(UpdateView):
    model = Day
    fields = ['days', 'opening_time', 'closing_time', 'opening_hours', 'closing_hours']

class DayDelete(DeleteView):
    model = Day

    def get_success_url(self):
        restaurants = self.object.restaurant_set.all()
        if restaurants.exists():
            restaurant = restaurants.first()
            return reverse_lazy('detail', kwargs={'retaurant_id': restaurant.pk})
        else:
            return reverse_lazy('index')

def add_day(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)

    days_count = restaurant.day_set.count()
    available_days = len(DAYS_OF_WEEK)

    if days_count == available_days:
        add_hours = False
    else:
        add_hours = True

    form = DayForm(request.POST)
    if add_hours and form.is_valid():
        new_day = form.save(commit=False)
        new_day.restaurant_id = restaurant_id
        new_day.save()
    else:
        form = DayForm()
    return render(request, 'restaurants/detail.html', {
        'restaurant': restaurant,
        'day_form': form,
    })

def add_review(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.restaurant_id = restaurant_id
        new_review.save()
    else:
        form = ReviewForm()

    return render(request, 'restaurants/detail.html', {
        'restaurant': restaurant,
        'review_form': form,
    })

class DeleteReview(DeleteView):
    model = Review
    success_url = '/restaurants'

# @login_required
# def reviews_index(request):
#   reviews = Review.objects.filter(user=request.user)
#   # You could also retrieve the logged in user's reviews
#   return render(request, 'reviews/index.html', { 'reviews': reviews })

def add_photo(request, restaurant_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, restaurant_id=restaurant_id)
        except Exception as e:
            print('An error occured uploading file to S3')
            print(e)
    return redirect('detail', restaurant_id=restaurant_id)
