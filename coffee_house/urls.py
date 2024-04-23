from django.urls import path
from coffee_house import views

app_name = 'coffee_house'

urlpatterns = [
    path('', views.all_coffee_house, name='home'),
    path('add_coffee_house/', views.add_coffee_house, name='add_coffee_house'),
    path('login/', views.login, name='auth'),
    path('logout/', views.logout, name='logout'),
    path('<slug:coffee_house_slug>/delete_coffee_house/', views.delete_coffee_house, name='delete_coffee_house'),
    path('<slug:coffee_house_slug>/edit/', views.edit_coffee_house, name='edit_coffee_house'),
    path('<slug:coffee_house_slug>/', views.coffee_house_detail, name='coffee_house_detail'),
]