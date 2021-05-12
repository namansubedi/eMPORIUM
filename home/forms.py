from django import forms
from django.forms import ModelForm
from .models import *
  
class productsform(forms.ModelForm):
  
    class Meta:
        model = products
        fields = '__all__'