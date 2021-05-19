from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.db.models import Q

from home.models import products
from .models import *
 

# Create your views here.
def addtocart(request):
    user = request.user
    buyer_id=user.username
    product_id=request.GET.get('prod_id')
    product=products.objects.get(id=product_id)
    c=Cart(buyer_id=buyer_id, product=product)
    c.save()
    
    return redirect('showcart')


def showcart(request):
 if request.user.is_authenticated:
    user = request.user
    buyer_id = user.username
    cart=Cart.objects.filter(buyer_id=buyer_id)
    product_in_cart=[product for product in Cart.objects.all() if product.buyer_id==buyer_id]
    totalamount=0
    amount=0
    charge=50
    
    #print(cart)
    #print(product_in_cart)
    
    if product_in_cart:
        for product in product_in_cart:
            temp=(product.quantity*product.product.price)
            amount=temp+amount
            totalamount=amount+charge
            
        noofitem=len(Cart.objects.filter(buyer_id=buyer_id))
                
            
        return render(request,'showcart.html',{"carts":cart,"totalamount":totalamount,"amount":amount,"noofitem":noofitem})
    else:
        return redirect("/")


    
    



def productdetail(request,slug):
    noofitem =0
    user=request.user
    buyer_id=user.username
    product=products.objects.filter(slug=slug)
    item_already_in_cart=False
    if request.user.is_authenticated:
        item_already_in_cart=Cart.objects.filter(Q(buyer_id=buyer_id) & Q(product=product[0])).exists()
        noofitem=len(Cart.objects.filter(buyer_id=buyer_id))
    return render(request,'productdetail.html',{'products':product,'item_already_in_cart':item_already_in_cart,'noofitem':noofitem})
    
    