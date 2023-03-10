from django.urls import path
from web_lib import views

urlpatterns = [
    path('', views.main, name='web_lib'),
    path('authors', views.authors, name='authors'),
    path('author/<uuid:pk>', views.author_id, name='author_id'),
    path('books', views.books, name='books'),
    path('about', views.about, name='about'),
    path('create_book', views.create_book, name='create_book'),
    path('update_book/<int:pk>', views.update_book, name='update_book'),
    path('delete_book/<int:pk>', views.delete_book, name='delete_book'),
]