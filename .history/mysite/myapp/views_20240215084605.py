from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.

def index(request):
    Book.objects.
    return HttpResponse('<h1>Hello Word</h1>')


def products(request):
    return HttpResponse('Products')