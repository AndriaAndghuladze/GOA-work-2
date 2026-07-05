from django.db import models

# Create your models here.
class Login(models.Model):
    name = models.CharField()
    last_name = models.CharField()
    age = models.IntegerField()
    email = models.EmailField()
    password = models.CharField
