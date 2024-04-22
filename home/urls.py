from django.urls import path
from . import views
from coffee_profile.views import add_menu
app_name = 'home'

urlpatterns = [
    path('', views.all_coffee_house, name='home'),
    path('<slug:coffee_house_slug>/menu/add/', add_menu, name='add_menu'),
    path('<slug:coffee_house_slug>/', views.coffee_house_detail, name='coffee_house_detail'),
    path('<slug:coffee_house_slug>/menu/<slug:menu_slug>/', views.menu_detail, name='menu_detail'),
    path('<slug:coffee_house_slug>/menu/<slug:menu_slug>/items/<slug:item_slug>/', views.item_detail, name='item_detail'),
]