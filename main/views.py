from django.shortcuts import render

from django.http import HttpResponse

from movies.models import Movie
from books.models import Book

def index(request):

    recent_items_limit = 6

    recent_books = Book.objects.all().exclude(date_finished__isnull=True).order_by('-date_finished')[:recent_items_limit]
    recent_movies = Movie.objects.all().order_by('-date_watched')[:recent_items_limit]

    context = {
        'recent_books': recent_books,
        'recent_movies': recent_movies,
    }
    
    return render(request, 'main/index.html', context)

def media_diet(request):

    recent_items_limit = 10
    recent_books = Book.objects.all().exclude(date_finished__isnull=True).order_by('-date_finished')[:recent_items_limit]
    recent_movies = Movie.objects.all().order_by('-date_watched')[:recent_items_limit]

    context = {
        'recent_books': recent_books,
        'recent_movies': recent_movies,
    }

    return render(request, 'main/media_diet.html', context)

