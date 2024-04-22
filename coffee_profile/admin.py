from django.contrib import admin

# Register your models here.
from .models import CoffeeHouse, Menu, MenuItem




# admin.site.register(CoffeeHouse)
# admin.site.register(Menu)
# admin.site.register(MenuItem)

@admin.register(CoffeeHouse)
class CoffeeHouseAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description', 'schedule', 'creation_date']
    prepopulated_fields = {'slug': ('name',)}
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'quantity', 'unit', 'menu', 'photo']
    prepopulated_fields = {'slug': ('name',)}