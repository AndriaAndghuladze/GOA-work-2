from django.db import models

# Create your models here.
class Login(models.Model):
    user = models.CharField()
    email = models.CharField()
    password = models.CharField()