from django.db import models

# Create your models here.

class Service(models.Model):
    img = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=150)
    desc = models.TextField()
    special = models.BooleanField()
    def __str__(self):
         return self.title
    

class Profile(models.Model):
    backimg=models.ImageField(upload_to='pics')
    proimg=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=100)
    desig=models.TextField()


    def __str__(self):
         return self.name

class Courses(models.Model):
    img = models.ImageField(upload_to='pics')
    title = models.CharField(max_length=150)
    desc = models.TextField()
    crash = models.BooleanField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
         return self.title
    

    
class Contacts(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    phone = models.BigIntegerField()
    messages = models.TextField()
    
    def __str__(self):
         return self.name