from django.forms import ModelForm
from .models import *

class PostForm(ModelForm):
    class Meta:
        model = Post
        #fields = '__all__'
        fields = ['image', 'title', 'text'] # user

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        #fields = ['name', 'quantity', 'price']
