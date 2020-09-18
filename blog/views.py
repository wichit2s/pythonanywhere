from django.shortcuts import render

from .models import Student

# Create your views here.
def index(req):
    students = Student.objects.all()
    return render(req, 'blog/index.html', { 'students': students })
