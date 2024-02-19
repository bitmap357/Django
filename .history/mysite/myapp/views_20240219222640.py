from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

# Create your views here.

def index(request):
    book_list = Book.objects.all()
    context = {
        'book_list':book_list
    }
    return render(request, 'myapp/index.html', context)


def detail(request, book_id):
    book = Book.objects.get(id=book_id)
    
    return render(request, 'myapp/detail.html', {'book':book})

def add_book(request):
    if request.method == 'POST':
        name = request.POST.get('name',)
        desc = request.POST.get('name',)
        desc = 
    return render(request, 'myapp/add_book.html')