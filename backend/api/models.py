from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    birthdate = models.DateField()
    # location ={
    #     'latitude': models.FloatField(),
    #     'longitude': models.FloatField(),
    #     'city': models.CharField(max_length=100)
    # }
    location = models.CharField(max_length=200)
    allergies = models.CharField(max_length=500)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email
