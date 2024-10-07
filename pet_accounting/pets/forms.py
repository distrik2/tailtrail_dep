# pets/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import PetProfile

class UserRegisterForm(UserCreationForm):
    telegram_id = forms.CharField(max_length=100)
    full_name = forms.CharField(max_length=100)
    phone_number = forms.CharField(max_length=20)
    pet_name = forms.CharField(max_length=100)
    pet_breed = forms.CharField(max_length=100)
    pet_age = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'telegram_id', 'full_name', 'phone_number', 'pet_name', 'pet_breed', 'pet_age']
