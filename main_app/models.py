from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


DAYS_OF_WEEK = (
    ('SU', 'Sunday'),
    ('MO', 'Monday'),
    ('TU', 'Tuesday'),
    ('WE', 'Wednesday'),
    ('TH', 'Thursday'),
    ('FR', 'Friday'),
    ('SA', 'Saturday'),
)

OPTIONS = (
    ('R_R', 'Restaurant Review'),
    ('A_R', 'Alternate Recommendation')
)

AM_PM_CHOICES = (
    ('AM', 'AM'),
    ('PM', 'PM'),
)

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zip_code = models.IntegerField()
    cuisine = models.CharField(max_length=25)
    dine_in = models.BooleanField(default=False)
    take_out = models.BooleanField(default=False)
    delivery = models.BooleanField(default=False)
    drive_thru = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'restaurant_id': self.id})

class Day(models.Model):
    days = models.CharField(
        max_length=2,
        choices=DAYS_OF_WEEK,
        default=DAYS_OF_WEEK[0][0]
    )
    opening_time = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(12)])
    opening_hours = models.CharField(max_length=2, choices=AM_PM_CHOICES, default=AM_PM_CHOICES[0][0])
    closing_time = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(12)])
    closing_hours = models.CharField(max_length=2, choices=AM_PM_CHOICES, default=AM_PM_CHOICES[0][0])
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return self.get_days_display()

    def get_absolute_url(self):
        return reverse('days_detail', kwargs={'pk': self.id})

class Review(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    review = models.CharField(
        max_length=300,
    )
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE
    )
    def __str__(self):
        return  f"{self.get_review_display()} on {self.created_at}"

    def get_absolute_url(self):
        return reverse('review_detail', kwargs={'pk': self.id})

class Photo(models.Model):
    url = models.CharField(max_length=200)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for restaurant_id: {self.restaurant_id} @{self.url}"