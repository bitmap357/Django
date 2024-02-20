from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Me
    model = Book
    fields = ['name', 'desc', 'price', 'book_image']