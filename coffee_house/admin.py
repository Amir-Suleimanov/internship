from django.contrib import admin

# Register your models here.
from .models import CoffeeHouse

@admin.register(CoffeeHouse)
class CoffeeHouseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'schedule', 'creation_date']
    prepopulated_fields = {'slug': ('name',)}