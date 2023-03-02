from django.shortcuts import render
from web_lib.models import Author, Book

def main(request):
    return render(request, 'web_lib/main.html')

def authors(request):
    all_authors = {'authors': Author.objects.all()}
    return render(request, 'web_lib/authors.html', all_authors)

def author_id(request, pk):
    author = Author.objects.get(pk=pk)
    books_amount = author.book_set.count()
    found_author= {'author': author, 'books_amount': books_amount}
    return render(request, 'web_lib/author_id.html', found_author)

def books(request):
    all_books = {'books': Book.objects.all()}
    return render(request, 'web_lib/books.html', all_books)

def about(request):
    return render(request, 'web_lib/about.html')
