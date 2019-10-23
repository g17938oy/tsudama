from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.order_by('price')
    return render(request, 'market/first.html', {'books':books})

def login(request):
    return render(request, 'market/login.html')

def home(request):
    return render(request, 'market/home.html')

def product(request):
    return render(request, 'market/product.html')

def talk(request):
    return render(request, 'market/talk.html')
