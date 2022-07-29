
from django.db import models


# Create your models here.

class Products(models.Model):

    name = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=200, null=True)
    ratings = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True)
    url = models.CharField(max_length=200, null=True)
    imageSrc = models.CharField(max_length=200, null=True)

    def __str__(self):  
       return self.name

  
class User(models.Model):
    username = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name