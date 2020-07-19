from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
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
 
class Hood(models.Model):
    locations = (
        ('Westlands', 'Westlands'),
        ('Parklands', 'Parklands'),
        ('Kilimani', 'Kilimani'),
        ('Machakos', 'Machakos'),
        ('Nakuru', 'Nakuru'),
        ('Kisumu', 'Kisumu'),
        ('Bungoma', 'Bungoma'),
        ('Ruaka', 'Ruaka'),
        ('Ruiru', 'Ruiru'),
        ('Kibera', 'Kibera'),
        ('Kitengela', 'Kitengela'),
        ('Athi River', 'Athi River'),        
        ('Thika', 'Thika'),
        ('Syokimau', 'Syokimau'),
        ('Utawala', 'Utawala'),
        ('Kasarani', 'Kasarani'),
        ('Ngong', 'Ngong'),
        ('Embu', 'Embu'),
        ('Runda', 'Runda'),
        ('Voi', 'Voi'),        
        ('Komarock', 'Komarock'), 
        ('Donholm', 'Donholm'),  
        ('Kileleshwa', 'Kileleshwa'),
        ('Mombasa', 'Mombasa'),       
    )
    name = models.CharField(max_length=100)
    image = CloudinaryField('image')
    residents = models.CharField(max_length=100)
    location_name = models.CharField(max_length=100, choices=locations)

    def save_hood(self):
        self.save()


    def delete_hood(self):
        self.delete()


    @classmethod
    def search_hood(cls, search_term):
        hood = Hood.objects.filter(location__name__icontains=search_term)
        return hood

    @classmethod
    def display_all_hoods(cls):
        return cls.objects.all()

    def __str__(self):
        return self.name

class Profile(models.Model):
    profile_picture = CloudinaryField('image')
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bio = models.CharField(max_length=100)
    full_names = models.CharField(max_length=300)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE, null=True)

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



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=300)
    hood = models.ForeignKey(Hood, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=65)

    def __str__(self):
        return self.title

    @classmethod
    def get_post(cls, id):
        post = Post.objects.filter(hood__pk=id)
        return post

class Business(models.Model):
    business_name = models.CharField(max_length=50)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    hood = models.ForeignKey(Hood,on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.business_name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()


    @classmethod
    def get_business(cls, id):
        business = Business.objects.filter(hood__pk=id)
        return business

    @classmethod
    def search_business(cls, search_term):
        business = Business.objects.filter(category__icontains=search_term)
        return business                                 