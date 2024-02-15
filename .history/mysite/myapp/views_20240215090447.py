from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.

def index(request):
    book_list = Book.objects.all()
    context = 
    return render(request, 'myapp/index.html')


def products(request):
    return HttpResponse('Products') 