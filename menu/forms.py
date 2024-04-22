from django import forms

from .models import Menu, MenuItem


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'coffee_house']

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'quantity', 'unit', 'menu', 'photo']
