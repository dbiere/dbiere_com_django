from django.db import models
from datetime import datetime

class Movie(models.Model):
    title = models.CharField(max_length=500, blank=False)
    year_released = models.IntegerField(blank=False)
    is_favorite = models.BooleanField(default=False)
    imdb_id = models.CharField(max_length=50, blank=False)
    date_watched = models.DateField(blank=False)
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.title + ' (' + str(self.year_released) + ')'