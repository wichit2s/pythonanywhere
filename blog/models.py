from django.db import models

# Create your models here.
class Student(models.Model):

    sid = models.Char

    def __str__(self):
        return f'{self.sid} {self.name}'