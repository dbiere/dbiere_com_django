from django.db import models
from datetime import datetime

class ResumeSummary(models.Model):
    overview = models.TextField(blank=False)
    qualifications = models.TextField(blank=False)

    def __str__(self):
        return 'Devon Biere Resume'

#--------------------------------------------------------------------------------------------------
# Skills

class SkillArea(models.Model):
    name = models.CharField(max_length=200, blank=False)
    display_order = models.IntegerField(blank=False)

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=200, blank=False)
    skill_area = models.ForeignKey('SkillArea', on_delete=models.CASCADE,)

    def __str__(self):
        return self.name

#--------------------------------------------------------------------------------------------------
# Jobs

class Company(models.Model):
    name = models.CharField(max_length=200, blank=False)

    def __str(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=200, blank=False)
    company = models.ForeignKey('Company', on_delete=models.CASCADE,)
    department = models.CharField(max_length=300)
    date_started = models.DateField(blank=False)
    date_ended = models.DateField()
    location = models.CharField(max_length=200, blank=False)
    description = models.TextField(blank=False)

    def __str__(self):
        return self.title

#--------------------------------------------------------------------------------------------------
# Patents

class Patent(models.Model):
    uspto_number = models.IntegerField(blank=False)
    title = models.TextField(blank=False)
    inventors = models.TextField(blank=False)
    assignee = models.TextField(blank=False)
    abstract = models.TextField(blank=False)
    date_filed = models.DateField(blank=False)
    date_granted = models.DateField(blank=False)
    continuation_of_uspto_number = models.IntegerField()

    def __str__(self):
        return self.uspto_number

#--------------------------------------------------------------------------------------------------