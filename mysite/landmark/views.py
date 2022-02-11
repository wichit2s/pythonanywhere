from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic.edit import FormView

from .models import *
from .forms import LandmarkForm

class LandmarkFormView(FormView):
    template_name = 'landmark/form.html'
    form_class = LandmarkForm
    #success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        #form.send_email()
        print('form_valid()')
        print(form.instance)
        return super().form_valid(form)

class LandmarkListView(generic.ListView):
    model = Landmark
    template_name = 'landmark/landmark_list.html'

    def get_context_data(self, **kwargs):
        context = super(LandmarkListView, self).get_context_data(**kwargs)
        context['new_var'] = 'value'
        context['form'] = LandmarkForm()
        return context

    def get_queryset(self):
        #return Landmark.objects.all()
        return Landmark.objects.all().order_by('-rating')

    def post(self, request, **kwargs):
        form = LandmarkForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print('form is invalid.')
        self.object_list = self.get_queryset()
        return super(LandmarkListView, self).render_to_response(self.get_context_data(**kwargs))

# Create your views here.
def login(request):
    print(f'request.method = {request.method}')
    if request.method == 'POST':
        #print(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        # User.objects.filter(username=username, password=password).first()
        u = authenticate(username=username, password=password)
        if u:
            auth_login(request, u)
            print('authenticate & logged in')
            return redirect('/landmarks/')

    return render(request, 'landmark/login.html')

def logout(request):
    auth_logout(request)
    return redirect('/')

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
                User.objects.create_user(username=username, password=password1)
                print(f'สร้าง username={username} password={password1} แล้ว')
            return redirect('/login/')
    return render(request, 'landmark/register.html')

def home(request):
    landmarks = Landmark.objects.all()
    sam = landmarks[0]
    phatam = landmarks[1]
    slides = [
        {"index": 0, "title": "title", "code":"", "subtitle": "subtitle"},
        {"index": 1, "title": "title", "subtitle": "subtitle"},
        {"index": 2, "title": "title", "subtitle": "subtitle"},
        {"index": 3, "title": "title", "subtitle": "subtitle"},
    ]
    """
    conda create --name landmarkwebvenv python=3.9.5
    conda activate landmarkwebvenv
    pip install jango==3.2.3 ipython Pillow
    """
    return render(request, 'landmark/home.html', {
        'sam': sam,
        'phatam': phatam,
        'landmarks': landmarks,
        'slides': slides,
    })

def slides(request):
    return render(request, 'landmark/slides.html', {
        'slides': Slide.objects.all()
    })
def oohome(request):
    landmarks = Landmark.objects.all()
    sam = landmarks[0]
    phatam = landmarks[1]
    return render(request, 'landmark/oohome.html', {
            'sam': sam,
            'phatam': phatam,
            'landmarks': landmarks,
        })

