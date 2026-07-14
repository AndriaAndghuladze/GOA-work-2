from django.db import models

# Create your models here.
class Register(models.Model):
    username = models.CharField()
    password = models.CharField()
    