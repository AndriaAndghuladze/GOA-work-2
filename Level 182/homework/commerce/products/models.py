from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField()
    price = models.CharField()
    category = models.CharField()