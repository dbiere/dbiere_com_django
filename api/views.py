from django.shortcuts import render

from movies.models import Movie

# REST
from rest_framework import viewsets
from .serializers import MovieSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('title')
    serializer_class = MovieSerializer



