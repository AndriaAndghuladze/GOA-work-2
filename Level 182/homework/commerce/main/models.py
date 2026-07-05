from django.db import models

# Create your models here.
class Review(models.Model):
    title = models.CharField()
    description = models.CharField()
    rating = models.IntegerField()