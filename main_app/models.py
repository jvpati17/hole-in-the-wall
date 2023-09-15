from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    # THIS UPDATES VIEW TO ASSIGN NEW RESTAURANT TO LOGGED IN USER
    # def form_valid(self, form):
    # # Assign the logged in user (self.request.user)
    # form.instance.user = self.request.user  # form.instance is the cat
    # # Let the CreateView do its job as usual
    # return super().form_valid(form)
