from django.db import models
from datetime import datetime

class Book(models.Model):
    title = models.CharField(max_length=500, blank=False)
    author = models.ManyToManyField('Author')
    year_published = models.IntegerField(blank=False)
    amazon_asin = models.CharField(max_length=100, blank=False)
    is_fiction = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)
    date_started = models.DateField(blank=False)
    date_finished = models.DateField(null=True, blank=True)
    comments = models.TextField(blank=True)
    # Properties
    _amazon_image_url = None

    def __str__(self):
        return self.title

    @property
    def amazon_image_url(self):
        return self._amazon_image_url
    
    @amazon_image_url.setter
    def amazon_image_url(self, value):
        self._amazon_image_url = value

#---------------------------------------------------------------------------------------------------

class Author(models.Model):
    display_name = models.CharField(max_length=200, blank=False)            # Ron Chernow
    formal_sort_name = models.CharField(max_length=200, blank=False)        # Chernow, Ron

    def __str__(self):
        return self.formal_sort_name

    class Meta:
        ordering = ['formal_sort_name']


