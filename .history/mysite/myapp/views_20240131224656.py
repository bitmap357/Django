from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1>Hello Word')


def products(request):
    return HttpResponse('Products')