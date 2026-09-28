# Create your views here.
from django.shortcuts import render
from .models import Book

def book_list(request):
 books=Book.objects.all()
 return render(request,'library/book_list.html',{'books':books})
from .models import Book

def book_list(request):
 books=Book.objects.all()
 return render(request,'library/book_list.html',{'books':books})
