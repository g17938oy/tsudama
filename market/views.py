from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.order_by('price')
    return render(request, 'market/book_list.html', {'books':books})
