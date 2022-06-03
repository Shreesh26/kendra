from itertools import product
from urllib import request, response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import *
from nlp.nlp import *
from upload.models import Area, File

class Search(APIView):
    @staticmethod 
    def get(request):
        data = request.data
        area=Area.objects.all()
        l=len(list(area.values()))
        arr=[0 for i in range(l)]
        for i in range(l):
            arr[i]=list(area.values())[i]['area']
        search=data['search']
        tag=associatedLabel(search, arr)
        print(tag['labels'][0])
        print(tag)
        file_name=File.objects.filter(name__icontains=search)
        print("here")
        associated_tag=Area.objects.filter(area=tag['labels'][0])[0]
        tag_search=File.objects.filter(area=associated_tag)
        search_data=file_name.union(tag_search)
        return Response(list(search_data.values()))