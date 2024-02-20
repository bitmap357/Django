from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    
    model = Book
    fields = ['name', 'desc', 'price', 'book_image']