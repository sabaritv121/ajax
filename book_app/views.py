from django.shortcuts import render

# Create your views here.

from .models import Author, Book

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})

def book_list(request, author_id):
    books = Book.objects.filter(author_id=author_id)
    return render(request, 'book_list.html', {'books': books})
####################