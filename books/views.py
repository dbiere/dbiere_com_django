from django.shortcuts import render

from django.conf import settings

from .models import Book

def index(request):
    old_books_start_year = 1992
    current_books = Book.objects.filter(date_finished__isnull=True).order_by('-date_started').prefetch_related('author')
    books = Book.objects.filter(date_finished__year__gt=old_books_start_year).order_by('-date_finished__year', 'title').prefetch_related('author')
    old_books = Book.objects.filter(date_finished__year__lte=old_books_start_year).order_by('title').prefetch_related('author')

    # Build context and return
    context = {
        'current_books': current_books,
        'books': books,
        'old_books': old_books,
        'old_books_start_year': old_books_start_year,
    }

    return render(request, 'books/index.html', context)

