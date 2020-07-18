from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Resident(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    def save_resident(self):
        self.save()    

    class Meta:
        ordering = ['first_name']
 
 class Profile(models.Model):
    profile_picture =          