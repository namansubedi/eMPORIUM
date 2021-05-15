from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.db.models import Q
from home.models import products
from .models import *
 

# Create your views here.
def cart1(request):
    return render(request, "cart.html")



def productdetail(request,slug):
    product=products.objects.filter(slug=slug)
    return render(request, "productdetail.html",{'products':product})