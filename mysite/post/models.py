from django.db import models

# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=300)
    text = models.TextField()

    def __str__(self):
        return f'POST: {self.title}'

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
