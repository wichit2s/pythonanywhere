from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def post(request):
    print(f'{request.method} post()')
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        #print(request.POST)
        #print(form.is_valid())
        if form.is_valid():
            form.save()
    else:
        form = PostForm()
    posts = Post.objects.all()
    return render(request, 'post/bootstrap5post.html', {
        'posts': posts,
        'form': form
    })

def login(request):
    if request.method == 'POST':
        #print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        # User.objects.filter(username=username, password=password).first()
        u = authenticate(username=username, password=password)
        if u:
            auth_login(request, u)
            print('authenticate & logged in')
            return redirect('/post/')

    return redirect('/post/')

def logout(request):
    auth_logout(request)
    return redirect('/post/')

def register(request):
    print(f'request.method = {request.method}')
    if request.method == 'POST':
        #print(request.POST)
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            u = User.objects.filter(username=username).first()
            if u:
                print(f'มีผู้ใช้ชื่อ {username} อยู่แล้ว')
                #u.set_password(password1)
                #u.save()
            else:
                u = User.objects.create_user(username=username, password=password1)
                auth_login(request, u)
                print(f'สร้าง username={username} password={password1} แล้ว')
            return redirect('/post/')
    return redirect('/post/')

def video(request):
    return render(request, 'post/video.html')
