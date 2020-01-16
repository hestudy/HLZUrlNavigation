from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import UrlsClass,Urls

# Create your views here.
def index(request):
    data = list(UrlsClass.objects.values())
    data = {
        'data':data
    }
    return JsonResponse(data)