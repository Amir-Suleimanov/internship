from django import forms

from .models import Menu, MenuItem


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ['name', 'coffee_house']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'oninput': "this.size=Math.max(this.value.length, 20)"})
        }

class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ['name', 'quantity', 'unit', 'menu', 'photo']
