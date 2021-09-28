from dataclasses import fields
from email.policy import default
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Register(UserCreationForm):
    email = forms.EmailField()
    profile_pic = forms.ImageField()

    class Meta:
        model = User

        fields= [
            'username',
            'profile_pic',
            'email',
            'password1',
            'password2',
        ]