from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import CoffeeHouse
from django.contrib.auth.models import AbstractUser

from .models import User


class UsersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
            }),
        }

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = AbstractUser


class CoffeeHouseForm(forms.ModelForm):
    class Meta:
        model = CoffeeHouse
        fields = ['name', 'schedule', 'description']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'oninput': "this.size=Math.max(this.value.length, 20)"}),
            'schedule': forms.TextInput(attrs={'class': 'form-control', 'oninput': "this.size=Math.max(this.value.length, 20)"}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'id':"discription", 'cols':"20", 'rows':"3"}),
        }
