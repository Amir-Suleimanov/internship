from django.urls import path
from . import views

app_name = 'coffee_profile'

urlpatterns = [
    path('', views.profile, name='profile'),
    path('add_coffee_house', views.coffeehouse_create, name='coffeehouse_create'),
    # path('<slug:c_h_slug>/menu/<slug:menu_slug>/', views.menu_detail, name='menu_detail'),
    # path('<slug:c_h_slug>/menu/<slug:menu_slug>/edit', views.edit_menu, name='edit_menu'),
    # другие URL-ы...
]
