from django.db import models

# Create your models here.
class Product(models.model):
    tietle = models.CharField()
    price = models.CharField()
    category = models.CharField()

