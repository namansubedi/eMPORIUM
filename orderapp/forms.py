from django import forms
from django.forms import ModelForm
from .models import *

class fulfillform(forms.ModelForm):

    class Meta:
        model = order_item
        fields = ['status']
#not used right now
class paymentform(forms.ModelForm):

    class Meta:
        model = payment_details
        fields = ['status']