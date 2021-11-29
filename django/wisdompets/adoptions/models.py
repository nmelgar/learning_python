from django.db import models
from django.db.models.fields import CharField

class Pet(models.Model):
    #use a tupple for sex_choices constant
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    #these are fields (name, submitter, species, breed, description, etc)
    name = models.CharField(max_length=100)
    submitter = models.CharField(max_length=100)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30, blank=True)
    description = models.TextField()
    #use sex_choices as constant for choices
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, blank=True)
    submission_date = models.DateTimeField()
    #use null to indicate that age is unknown, using blank will result as ZERO
    age = models.IntegerField(null=True)
    #in a many to many field the
    #1st argument, model is related to as a string
    vaccinations = models.ManyToManyField('Vaccine', blank=True)

class Vaccine(models.Model):
    name = models.CharField(max_length=50)


