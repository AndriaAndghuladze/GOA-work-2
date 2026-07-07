from django.db import models

# Create your models here.
class Bmw(models.Model):
    model = models.CharField()
    year = models.IntegerField()
    price = models.IntegerField()