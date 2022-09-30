from django.shortcuts import render
import json
import requests
from itertools import islice
from .models import Test
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

        
@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'test': '/show/'
        },
        ]
    return Response(route=Fzz)
    
def get_data(request):
    url = f'https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty'
    response = requests.get(url)
    data = response.json()

    top_100 = islice(data, 3)
    for item in top_100:
        print(item)
        url = f'https://hacker-news.firebaseio.com/v0/item/{item}.json?print=pretty'
        response = requests.get(url)
        data = response.json()
        print(data)
        for i in top_100:
            new = Test(
                title = i
            )
            new.save()
    all = Test.objects.all()
    context = {
        "all": all
    }
 
        
    return render(request, 'api.html', context)
    
