from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('/add', views.add_menu, name='add_menu'),
    path('<slug:menu_slug>/', views.menu_detail, name='menu_detail'),
    path('<slug:menu_slug>/items/<slug:item_slug>/', views.item_detail, name='item_detail')
]