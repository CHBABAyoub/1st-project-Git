from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Index (request):
       return HttpResponse ('hello world')
def Item(request):
       return HttpResponse ('how are you doing')
