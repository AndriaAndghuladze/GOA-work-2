from django.db import models

# Create your models here.
class Main(models.model):
    title = models.CharField()
    price = models.CharField()
    category = models.CharField()