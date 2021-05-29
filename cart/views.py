from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.db.models import Q

from home.models import products
from .models import *



def buynow(request,slug):
    user = request.user # this means the logged-in user
    username=user.username
    product=products.objects.get(slug=slug)
    cart = Cart.objects.filter(buyer_id=username)
    for item in cart:
        item.delete()
    buy=Cart(buyer_id=username,product=product)
    buy.save()
    return redirect('showcart')

 
def delete(request,id):
    user = request.user # this means the logged-in user
    username=user.username
    product=products.objects.get(id=id)
    if product.seller_id == username:
        product.delete()
    return redirect('myproducts')
    
 

# Create your views here.
def addtocart(request):
    user = request.user # this means the logged-in user
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
    totalamount=0
    amount=0
    charge=50
    
    #print(cart)

    
    if cart:
        for product in cart:
            temp=(product.quantity*product.product.price)
            amount=temp+amount
            totalamount=amount+charge
            
        noofitem=len(Cart.objects.filter(buyer_id=buyer_id))
                
            
        return render(request,'showcart.html',{"carts":cart,"totalamount":totalamount,"amount":amount,"noofitem":noofitem})
    else:
        return render(request,"emptyproduct.html")

    
    



def productdetail(request,slug):
    noofitem =0
    user=request.user
    buyer_id=user.username
    product=products.objects.filter(slug=slug)
    seller=product[0].seller_id
    stock_quantity=product[0].stock
   # print(stock_quantity)
    is_item_in_cart=False
    if request.user.is_authenticated:
        is_item_in_cart=Cart.objects.filter(Q(buyer_id=buyer_id) & Q(product__in=product)).exists()
        noofitem=(Cart.objects.filter(buyer_id=buyer_id)).count()
    return render(request,'productdetail.html',
                  {'products':product,'is_item_in_cart':is_item_in_cart,'noofitem':noofitem,'seller':seller,'stock_quantity':stock_quantity})
    
    
