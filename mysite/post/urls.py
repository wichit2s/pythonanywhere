from django.urls import path
from .views import *

urlpatterns = [
    path('', post),
    path('login/', login),
    path('logout/', logout),
    path('register/', register),
    path('video/', video),
    path('api/deletepost/<int:id>/', deletepost)
]
