from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout as logout_user
from django.contrib.auth import login as login_user
from django.contrib.auth.models import User, AnonymousUser
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .models import Student, Lecturer

# Create your views here.
def index(req):
    return render(req, 'blog/index.html')

def course(req):
    return render(req, 'blog/course.html')

def aj(req):
    aj = Lecturer.objects.first()
    return render(req, 'blog/aj.html', { "aj": aj })

@login_required(login_url="/login")
def ajedit(req):
    aj = Lecturer.objects.first()
    if req.method == 'POST':
        aj.name = req.POST['name']
        aj.room = req.POST['room']
        aj.extension = req.POST['extension']
        aj.save()
    return render(req, 'blog/aj-edit.html', { "aj": aj })

def students(req):
    students = Student.objects.all()
    return render(req, 'blog/students.html', { 'students': students })

def studentspagination(req):
    students = Student.objects.all()
    paginator = Paginator(students, 10) 

    page_number = req.GET.get('page')
    page = paginator.get_page(page_number)
    return render(req, 'blog/studentspagination.html', { 'page': page })

def login(req):
    if req.method == 'POST':
        try:
            user = User.objects.get(email=req.POST['email'])
            user = authenticate(username=user.username, password=req.POST['password'])
            if user:
                login_user(req, user)
                #return redirect('/')
                return redirect(req.POST['next_url'])
            else:
                messages.error(req, 'รหัสผ่านไม่่ถูกต้อง')

        except:
            messages.error(req, 'ไม่มี email นี้ในระบบ')

    next_url = '/'
    if req.method == 'GET' and 'next' in req.GET:
        next_url = req.GET['next']

    return render(req, 'blog/login.html', { "next_url": next_url })

def sketchy(req):
    return render(req, 'blog/sketch.html')

def logout(req):
    logout_user(req)
    return redirect('/')
