from django.contrib import admin
from django.urls import path
from blog import views as blogview
#from pokemon import views as pokemonview

urlpatterns = [
    path('', blogview.index),
    path('course', blogview.course),
    path('aj', blogview.aj),
    path('ajedit', blogview.ajedit),
    path('students', blogview.students),
    path('studentspagination', blogview.studentspagination),
    path('login', blogview.login),
    path('logout', blogview.logout),
    path('sketchy', blogview.sketchy),
    #path('pokemon', pokemonview.index),
    #path('ab/<str:fn>', pokemonview.atimesb),
    path('admin/', admin.site.urls),
]
