from django.shortcuts import render

from learning.models import Training, TrainingCategory, TrainingSource
from movies.models import Movie

# REST
from rest_framework import viewsets
from .serializers import MovieSerializer
from .serializers import TrainingSerializer
from .serializers import TrainingCategorySerializer
from .serializers import TrainingFullSerializer
from .serializers import TrainingSourceSerializer

#--------------------------------------------------------------------------------------------------
# Movies

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all().order_by('title')
    serializer_class = MovieSerializer

#--------------------------------------------------------------------------------------------------
# Learning

class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all().order_by('-date_started')
    serializer_class = TrainingSerializer

class TrainingFullViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all().order_by('-date_started') \
        .prefetch_related('source') \
        .prefetch_related('category') \
        .prefetch_related('tags')
    serializer_class = TrainingFullSerializer

class TrainingSourceViewSet(viewsets.ModelViewSet):
    queryset = TrainingSource.objects.all()
    serializer_class = TrainingSourceSerializer

class TrainingCategoryViewSet(viewsets.ModelViewSet):
    queryset = TrainingCategory.objects.all()
    serializer_class = TrainingCategorySerializer


