from django.contrib import admin
from django.urls import path
from blog import views as blogview

urlpatterns = [
    path('', blogview.index),
    path('admin/', admin.site.urls),
]
