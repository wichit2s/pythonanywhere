from django.shortcuts import render

from .models import Landmark

# Create your views here.
def home(request):
    landmarks = Landmark.objects.all()
    sam = landmarks[0]
    phatam = landmarks[1]
    return render(request, 'landmark/home.html', {
            'sam': sam,
            'phatam': phatam,
            'landmarks': landmarks,
        })
