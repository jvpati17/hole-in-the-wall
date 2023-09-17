from django.shortcuts import render, redirect
from .models import Restaurant
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

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
    return render(request, 'restaurants/detail.html', {
        'restaurant': restaurant
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
    fields = ['opening_time', 'closing_time', 'days', 'dine_in', 'take_out', 'delivery', 'drive_thru']

class RestaurantDelete(DeleteView):
    model = Restaurant
    success_url = '/restaurants'

def assoc_day(request, restaurant_id, day_id):
    Restaurant.objects.get(id=restaurant_id).days.add(day_id)
    return redirect('detail', restaurant_id=restaurant_id)

def unassoc_day(request, restaurant_id, day_id):
    Restaurant.objects.get(id=restaurant_id).days.remove(day_id)
    return redirect('detail', restaurant_id=restaurant_id)

# @login_required
# def reviews_index(request):
#   reviews = Review.objects.filter(user=request.user)
#   # You could also retrieve the logged in user's reviews
#   return render(request, 'reviews/index.html', { 'reviews': reviews })
