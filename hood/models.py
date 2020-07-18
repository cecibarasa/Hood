from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


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
    profile_picture = CloudinaryField('image')
    user = models, OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.CharField(max_length=100)
    full_names = models.CharField(max_length=300)

    def __str__(self):
        return self.user

    def save_profile(self):
        self.save()

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()            