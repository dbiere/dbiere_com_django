from django.shortcuts import render

from learning.models import Training, TrainingCategory, TrainingSource
from movies.models import Movie

# REST
from rest_framework import viewsets
from .serializers import MovieSerializer
from .serializers import TrainingSerializer, TrainingCategorySerializer, TrainingSourceSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('title')
    serializer_class = MovieSerializer

class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all().order_by('-date_started') \
        .prefetch_related('source') \
        .prefetch_related('category') \
        .prefetch_related('tags')
    serializer_class = TrainingSerializer

class TrainingSourceViewSet(viewsets.ModelViewSet):
    queryset = TrainingSource.objects.all()
    serializer_class = TrainingSourceSerializer

class TrainingCategoryViewSet(viewsets.ModelViewSet):
    queryset = TrainingCategory.objects.all()
    serializer_class = TrainingCategorySerializer


