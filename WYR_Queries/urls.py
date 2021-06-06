from django.urls import path
from .views import pageIndex
from . import views

urlpatterns = [
    path('', pageIndex.index, name='index'),
    path('userIndex/', pageIndex.userIndex, name='userIndex'),
    path('api/', views.api, name='api'),
    path('CreateQueries/', views.CreateQueries, name='CreateQueries'),
    
]
