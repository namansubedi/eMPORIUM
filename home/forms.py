from django import forms
from django.forms import ModelForm
from .models import *
  
class productsform(forms.ModelForm):
  
    class Meta:
        model = products
        fields = ['name', 'category', 'price', 'brand', 'image', 'description', 'stock', 'detail']

class profilesform(forms.ModelForm):

    class Meta:
        model = profiles
        fields = ['is_seller']