from django.db import models

# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    knownFor = models.TextField()
    bio = models.TextField()
    imageURL = models.TextField()
