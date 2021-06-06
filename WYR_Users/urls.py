from django.contrib.auth import logout
from django.urls import path
from . import views

urlpatterns = [
    path('', views.user, name='user'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.register, name='register'),
]
