from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.order_by('price')
    return render(request, 'market/home.html', {'books':books})
