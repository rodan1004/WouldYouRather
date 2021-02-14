from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Queries
import json
from .serilizers import QuerySerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

# from django.core.serializers import json

from django.core import serializers

def data_json():
    titles = Queries.objects.values('Topic').distinct()
    # titles_json = serializers.serialize('json', titles, fields('Topic'))
    with open('static\\static_files\\index\\topic.json', 'w') as file:
        data = json.dumps(list(titles))
        # print(data, file=file)
    # print(titles)
    

def home(request):
    return render(request, 'Querie/home.html')

def index(request, query_title):
    queries = Queries.objects.all()
    page = Queries.objects.filter(Topic=str(query_title))
    
    # print(page)
    # data_json()
    return render(request, 'Querie/index.html', {'queries': page})

def topic(request):
    data_json()
    
    with open('static\\static_files\\index\\topic.json', 'r') as file:
        data = json.loads(file)
    JsonResponse({'data': data})

@api_view(['GET'])
def querycreator(request):
    queries = Queries.objects.all()
    serializer = QuerySerializers(queries, many=True)
    return Response(serializer.data)


