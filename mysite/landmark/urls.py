from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('login/', login),
    path('logout/', logout),
    path('register/', register),
    path('slides/', slides),
    path('oo/', oohome),
    path('landmarks/', LandmarkListView.as_view(), name='landmarks'),
]
