from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name
    
class Landmark(models.Model):
    category    = models.ForeignKey(Category,  on_delete=models.CASCADE, null=True, blank=True)
    image       = models.CharField(max_length=300)
    title       = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    rating      = models.FloatField(default=0.0)
    reviews     = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} {self.rating} {self.reviews}'
