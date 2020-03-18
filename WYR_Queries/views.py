from django.shortcuts import render
from django.http import HttpResponse
from .models import Queries


# Create your views here.

def index(request):
    queries = Queries.objects.all()
    return render(request, 'Querie/index.html', {'queries': queries})
    

