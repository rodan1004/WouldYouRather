from django.shortcuts import render
from django.http import HttpResponse
from .models import Queries, Categories


# Create your views here.

def index(request):
    queries = Queries.objects.all()
    categories = Categories.objects.all()
    return render(request, 'Querie/index.html', {'queries': queries}, {'categories': categories})
    

