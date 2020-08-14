from django.db import models

# Create your models here.

class Service(models.Model):
    img = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=150)
    desc = models.TextField()
    special = models.BooleanField()

class Profile(models.Model):
    backimg=models.ImageField(upload_to='pics')
    proimg=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=100)
    desig=models.TextField()
