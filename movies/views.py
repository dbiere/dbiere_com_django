from django.shortcuts import render

from .models import Movie

def index(request):
    old_movies_start_year = 1992
    movies = Movie.objects.all().filter(date_watched__year__gt=old_movies_start_year).order_by('-date_watched__year', 'title')
    old_movies = Movie.objects.filter(date_watched__year__lte=old_movies_start_year).order_by('title')

    context = {
        'movies': movies,
        'old_movies': old_movies,
        'old_movies_start_year': old_movies_start_year,
    }

    return render(request, 'movies/index.html', context)

