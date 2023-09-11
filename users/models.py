from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    city= models.CharField(max_length=20)
    


