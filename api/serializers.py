from rest_framework import serializers

from learning.models import Training, TrainingCategory, TrainingSource
from movies.models import Movie

# Serializer info
# https://www.django-rest-framework.org/api-guide/serializers/
# ModelSerializer - fields correspond directly to Model fields
# HyperlinkedModelSerializer - includes url field instead of id

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # Must include either
        # fields = [] to indicate which fields to include or
        # exclude = [] to indicate which fields to exclude
        fields = ['id', 'title', 'year_released', 'imdb_id', 'date_watched']

class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        exclude = []

class TrainingSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingSource
        exclude = []

class TrainingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingCategory
        exclude = []


