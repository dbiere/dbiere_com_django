from django.db import models

from taggit.managers import TaggableManager

# Online or in-person classes, trainings, bootcamps, lessons, etc.
class Training(models.Model):
    title = models.CharField(max_length=500, blank=False)
    year_published = models.IntegerField(blank=False)
    source = models.ForeignKey('TrainingSource', on_delete=models.RESTRICT)
    trainer = models.CharField(max_length=500, blank=False)
    url = models.CharField(max_length=2000, blank=False)
    date_started = models.DateField(blank=False)
    category = models.ForeignKey('TrainingCategory', on_delete=models.RESTRICT)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True) # min 0.0 -> max 5.0
    notes = models.TextField()
    tags = TaggableManager()

    def __str__(self):
        return self.source.name + ": " + self.title + ' (' + str(self.year_published) + ')'

# Udemy, YouTube, Pluralsight, Khan Academy, etc.
class TrainingSource(models.Model):
    name = models.CharField(max_length=500, blank=False)
    url = models.CharField(max_length=2000, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.name

# Art, Music, Computer Science, Math, Data Science, Electronics, Game Development, Programming, Life, Database, etc.
class TrainingCategory(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.name
