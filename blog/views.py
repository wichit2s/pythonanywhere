from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout as logout_user
from django.contrib.auth import login as login_user
from django.contrib.auth.models import User, AnonymousUser

from .models import Student

# Create your views here.
def index(req):
    return render(req, 'blog/index.html')

def course(req):
    return render(req, 'blog/course.html')

def aj(req):
    return render(req, 'blog/aj.html')

def students(req):
    students = Student.objects.all()
    return render(req, 'blog/students.html', { 'students': students })

def login(req):
    if req.method == 'POST':
        user = User.objects.get(email=req.POST['email'])
        user = authenticate(username=user.username, password=req.POST['password'])
        if user:
            login_user(req, user)
            return redirect('/')

    else:
        return render(req, 'blog/login.html')

def sketchy(req):
    return render(req, 'blog/sketch.html')

def logout(req):
    logout_user(req)
    return redirect('/')
