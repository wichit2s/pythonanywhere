from django.forms import ModelForm
from .models import *

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class LandmarkForm(ModelForm):
    class Meta:
        model = Landmark
        fields = '__all__'

