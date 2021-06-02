from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.db.models import Q
from home .models import products
from .models import *

def pluscart(request):
    if request.method=='GET':
        user = request.user
        buyer_id = user.username
        product_id=request.GET['product_id']
        product=products.objects.get(id=product_id)
        cart=Cart.objects.get(Q(buyer_id=buyer_id) & Q(product=product))
        if product.stock<=cart.quantity:
            #print(cart.quantity)
            cart.save()
            totalamount=0
            amount=0
            charge=50
            a=Cart.objects.filter(buyer_id=buyer_id)
            
            for product in a:
                temp=(product.quantity*product.product.price)
                amount=temp+amount
                totalamount=amount+charge
            data={
                'quantity':cart.quantity,
                'amount':amount,
                'totalamount':totalamount,
              }
            
                
            
            return JsonResponse(data)
        
    
        else:
            cart.quantity+=1
            print(cart.quantity)
            cart.save()
            totalamount=0
            amount=0
            charge=50
            a=Cart.objects.filter(buyer_id=buyer_id)
            
            for product in a:
                temp=(product.quantity*product.product.price)
                amount=temp+amount
                totalamount=amount+charge
            data={
                'quantity':cart.quantity,
                'amount':amount,
                'totalamount':totalamount,
            
                
            }
            return JsonResponse(data)
        
    
def minuscart(request):
    if request.method=='GET':
        user = request.user
        buyer_id = user.username
        product_id=request.GET['product_id']
        product=products.objects.get(id=product_id)
        cart=Cart.objects.get(product=product,buyer_id=buyer_id)
        cart.quantity-=1
        cart.save()
        amount=0
        charge=50
        
        
        for item in Cart.objects.filter(buyer_id=buyer_id):
            temp=(item.quantity*item.product.price)
            amount=temp+amount
            totalamount=amount+charge
        data={
            'quantity':cart.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
        
    
    
def deletecart(request,slug):
    user = request.user # this means the logged-in user
    username=user.username
    cart= Cart.objects.filter(buyer_id=username)
    for item in cart:
        if item.product.slug==slug:
            item.delete()
    return redirect('showcart')
    

            



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

def addtocarts(request,slug):
 if request.user.is_authenticated:   
    user = request.user # this means the logged-in user
    buyer_id=user.username
    
    product=products.objects.get(slug=slug)
    seller=product.seller_id
    print(product.stock)

    is_item_in_cart=Cart.objects.filter(Q(buyer_id=buyer_id) & Q(product=product))
    c=Cart(buyer_id=buyer_id, product=product)
    if is_item_in_cart:
        return redirect('showcart')
    elif user.username==seller:
        return redirect('productdetail',slug=product.slug)
    elif product.stock==0:
        return redirect('productdetail',slug=product.slug)
    else:
    
        c.save()
    
        return redirect('showcart')
 else:
     return redirect('login')


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
            if product.quantity==0:
                return redirect('deletecart',slug=product.product.slug)
            temp=(product.quantity*product.product.price)
            amount=temp+amount
            totalamount=amount+charge
            print(product.quantity)
            
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
    
    
