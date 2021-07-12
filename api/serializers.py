from rest_framework import serializers

from taggit.serializers import TagListSerializerField, TaggitSerializer

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

class TrainingSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingSource
        exclude = []

class TrainingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingCategory
        exclude = []

class TrainingSerializer(serializers.ModelSerializer):

    tags = TagListSerializerField()

    class Meta:
        model = Training    
        fields = ['id', 'title', 'year_published', 'trainer', 'url', 'date_started',
            'rating', 'is_complete', 'notes',
            'source', 'category', 'tags'
            ]

class TrainingFullSerializer(serializers.ModelSerializer):

    training_source = TrainingSourceSerializer(source='source', many=False)
    training_category = TrainingCategorySerializer(source='category', many=False)

    tags = TagListSerializerField()

    class Meta:
        model = Training
        fields = ['id', 'title', 'year_published', 'trainer', 'url', 'date_started',
            'rating', 'is_complete', 'notes',
            'training_source',
            'training_category',
            'tags'
            ]

'''
    title = models.CharField(max_length=500, blank=False)
    year_published = models.IntegerField(blank=False)
    source = models.ForeignKey('TrainingSource', on_delete=models.RESTRICT)
    trainer = models.CharField(max_length=500, blank=False)
    url = models.CharField(max_length=2000, blank=False)
    date_started = models.DateField(blank=False)
    category = models.ForeignKey('TrainingCategory', on_delete=models.RESTRICT)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True) # min 0.0 -> max 5.0
    is_complete = models.BooleanField(default=False)
    notes = models.TextField()

    tags = TaggableManager()
'''



