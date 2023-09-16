from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

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
