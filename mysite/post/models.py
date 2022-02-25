from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=300)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'POST: {self.title}'

class Point(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    point = models.IntegerField(default=0)

    def __str__(self):
        return f'point ของ {self.user.username} เป็น {self.point}'

class Product(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=300)
    detail = models.TextField()
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)

    def total(self):
        t = self.quantity * self.price
        return t

    def __str__(self):
        return f'POST: {self.name}'
