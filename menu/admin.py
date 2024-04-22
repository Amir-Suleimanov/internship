from django.contrib import admin

from .models import Menu, MenuItem

# Register your models here.


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'quantity', 'unit', 'menu', 'photo']
    prepopulated_fields = {'slug': ('name',)}