from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('login/', views.Login, name='auth'),
    path('logout/', views.Logout, name='logout')
    # path('', )
]