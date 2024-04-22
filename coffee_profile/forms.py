from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import CoffeeHouse, Menu, MenuItem
from django.contrib.auth.models import AbstractUser


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


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'coffee_house']

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'quantity', 'unit', 'menu', 'photo']
