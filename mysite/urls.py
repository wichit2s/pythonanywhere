from django.contrib import admin
from django.urls import path
from blog import views as blogview
from pokemon import views as pokemonview

urlpatterns = [
    path('', blogview.index),
    path('pokemon', pokemonview.index),
    path('admin/', admin.site.urls),
]