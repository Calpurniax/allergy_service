from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    birthdate = models.CharField()   
    location = models.CharField(max_length=200)
    latitude =models.FloatField(),
    longitude = models.FloatField(),
    allergies = models.CharField(blank=True, max_length=500)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.email
