from django.db import models

# Create your models here.
class Phone(models.Model):
    brand = models.CharField()
    price = models.IntegerField()