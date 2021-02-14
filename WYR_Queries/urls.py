from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('querycreator', views.querycreator, name='querycreator'),
    path('<query_title>', views.index, name='index'),
]
