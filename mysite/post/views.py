from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User, AnonymousUser
from django.shortcuts import render, redirect
from .forms import *

# Create your views here.
def post(request):
    print(f'{request.method} post()')
    point = None
    if request.method == 'POST':
        if request.user.is_authenticated:
            print(request.user.username)
            point = Point.objects.filter(user=request.user).first()
            if point:
                point.point += 2
                point.save()
            else:
                point = Point(user=request.user, point=2)
                point.save()
        else:
            print('ไม่ได้ login ก่อน post')
        form = PostForm(request.POST, request.FILES)
        #print(request.POST)
        #print(form.is_valid())
        if form.is_valid():
            form.instance.user = request.user
            form.save()
    else:
        form = PostForm()
    posts = Post.objects.all()
    point = None
    if request.user.is_authenticated:
        point = request.user.point_set.first()
    return render(request, 'post/bootstrap5post.html', {
        'posts': posts,
        'form': form,
        'point': point
    })

def deletepost(request, id):
    print(f' โดนสั่งลบ post id = {id}')
    if not request.user.is_authenticated:
        print(f'ผู้ใช้ไม่ได้ login')
    else:
        post = Post.objects.filter(pk=id).first()
        if post and post.user == request.user:
            post.delete()
    return redirect('/post/')

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
