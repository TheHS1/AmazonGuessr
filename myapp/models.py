from django.db import models
import uuid


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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=200, null=True)
    password = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Games(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    modifier = models.FloatField(default=1.0)
    totalScore = models.IntegerField(default=0)
    roundNumber = models.IntegerField(default=1)
    hintsUsed = models.IntegerField(default=0)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.name
