from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class HoodForm(forms.ModelForm):
    class Meta:
        model = Hood
        fields = ['name', 'location_name','image',]

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username","email","password1", "password2"]

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email')


class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['full_names', 'profile_picture', 'bio']


class BusinessForm(forms.ModelForm):
    class Meta:
        model  = Business
        fields = ['business_name','address','owner','category']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description']