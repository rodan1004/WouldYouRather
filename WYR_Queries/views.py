from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Queries
from .forms import QueryForm
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
    

class pageIndex:
    def index(request):
        queries = Queries.objects.all()
        # page = Queries.objects.filter(Topic=str(query_title))
        
        return render(request, 'Querie/index.html', {'queries': queries})
    
    def userIndex(request):
        queries = Queries.objects.all()
        
        return render(request, 'Querie/userIndex.html', {'queries': queries})



@api_view(['GET'])
def api(request):
    queries = Queries.objects.all()
    serializer = QuerySerializers(queries, many=True)
    return Response(serializer.data)


def CreateQueries(request):
    queryform = QueryForm() 
    if request.method == 'POST':
        queryform = QueryForm(request.POST, request.FILES)
        if queryform.is_valid():
            title_question = queryform.cleaned_data.get('Title')
            first_question = queryform.cleaned_data.get('Query1')
            second_question = queryform.cleaned_data.get('Query2')
            first_image = queryform.cleaned_data.get('Image1')
            second_image = queryform.cleaned_data.get('Image2')
            
            queries = Queries.objects.create(
                Topic=title_question,
                Q1=first_question,
                Q2=second_question,
                Qimg1=first_image,
                Qimg2=second_image
            )
            
            queries.save()
            print(queries)
        

    return render(request, 'Querie/CreateQueries.html', {'form': queryform})


