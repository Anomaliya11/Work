from django.shortcuts import render
from web_lib.models import Author, Book
def main(request):
    return render(request, 'web_lib/main.html')

def authors(request):
    all_authors = {'authors': Author.objects.all()}
    return render(request, 'web_lib/authors.html', all_authors)

def books(request):
    all_books = {'books': Book.objects.all()}
    return render(request, 'web_lib/books.html', all_books)

def about(request):
    return render(request, 'web_lib/about.html')
