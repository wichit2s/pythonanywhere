from django.db import models

# Create your models here.
class Student(models.Model):

    sid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300, default='')
    email = models.EmailField(max_length=400)
    nick = models.CharField(max_length=100, default='')
    pythonanywhere = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    gpa = models.FloatField(default=4.00)

    def __str__(self):
        return f'{self.sid} {self.name}'

class Lecturer(models.Model):

    name = models.CharField(max_length=300, default='ดร.วิชิต สมบัติ')
    room = models.CharField(max_length=20, default='SC204')
    extension = models.CharField(max_length=20, default='4446')

    def __str__(self):
        return f'{self._id} {self.name}'
