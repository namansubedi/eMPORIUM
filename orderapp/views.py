from django.shortcuts import render
from cart.models import Cart

# Create your views here.

def order(request):
    username = request.user.username    
    cart = Cart.objects.filter(buyer_id = username)
    context = {
        'carts': cart
    }
    
    return render(request , 'myorder.html',context)


def checkout(request):
     username = request.user.username   
     cart = Cart.objects.filter(buyer_id = username)
     context = {
        'carts':cart
    }
     return render (request,'checkout.html',context)