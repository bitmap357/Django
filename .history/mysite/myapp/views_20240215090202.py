from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.

def index(request):
    book_list = Book.objects.all()
    return render


def products(request):
    return HttpResponse('Products') 