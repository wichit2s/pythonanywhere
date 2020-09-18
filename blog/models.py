from django.db import models

# Create your models here.
class Student(models.Model):

    sid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, default='')
    nick = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=400)
    gpa = models.FloatField(default=4.00)

    def __str__(self):
        return f'{self.sid} {self.name}'
