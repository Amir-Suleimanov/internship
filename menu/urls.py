from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    path('add/', views.add_menu, name='add_menu'),
    path('<slug:menu_slug>/', views.menu_detail, name='menu_detail'),
    path('<slug:menu_slug>/edit_menu', views.edit_menu, name='edit_menu'),
    path('<slug:menu_slug>/delete_menu', views.delete_menu, name='delete_menu'),
    path('<slug:menu_slug>/items/add/', views.item_add, name='item_add'),
    path('<slug:menu_slug>/items/<int:item_id>/', views.item_detail, name='item_detail'),
    path('<slug:menu_slug>/items/<int:item_id>/edit', views.item_edit, name='item_edit'),
    path('<slug:menu_slug>/items/<int:item_id>/delete/', views.delete_item, name='delete_item'),
]