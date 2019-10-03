from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=300)
    hp = models.IntegerField()
    gender = models.CharField(max_length=20)
    image = models.ImageField('/media/')
