from itertools import product
from urllib import request, response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import *
from nlp.nlp import document_summary
import PyPDF2

class Upload (APIView):
    @staticmethod
    def post(request):
        name=request.data["name"]
        file=request.data["file"]
        area1=request.data['area1']
        area2=request.data['area2']
        area_1=Area.objects.get(area=area1)
        area_2=Area.objects.get(area=area2)
        file=File(name=name, file=file)
        file.save()
        file.area.add(area_1)
        file.area.add(area_2)
        summary=""
        pdfFileObj = open("media/"+file.file.name, 'rb') 
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        print(pdfReader.numPages)
        for i in range(pdfReader.numPages):
            pageObj= pdfReader.getPage(i)
            text=document_summary(pageObj.extractText())
            summary=summary+" "+text[0]['summary_text']
        pdfFileObj.close()
        summary_object=Summary(file=file, summary=summary)
        summary_object.save()
        
        return Response("Success")


"""class Summary (APIView):
    @staticmethod
    def post(request):

        pdfFileObj = open(file, 'rb') 
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        print(pdfReader.numPages) 
        pageObj = pdfReader.getPage(0) 
        print(pageObj.extractText()) 
        pdfFileObj.close() """