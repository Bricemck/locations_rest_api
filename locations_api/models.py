from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=255)

class Location(models.Model):   
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)