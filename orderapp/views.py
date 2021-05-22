from django.shortcuts import render, redirect
from cart.models import Cart
from orderapp.models import order, payment_details, order_item
from home.models import profiles
from django.contrib import messages
import random

# Create your views here.

def orderdetails(request, orderid):
    order1 = order.objects.get(order_id = orderid)
    orderitem = order_item.objects.filter(order_id =  orderid)
    payment = payment_details.objects.get(order_id = orderid)
    context = {
        'orders': order1,
        'orderitem': orderitem,
        'payment': payment,
    }
    return render(request, 'orderdetails.html', context)

def esewa(request):
    pass

def myorder(request):
    username = request.user.username  
    order_item1 =  order_item.objects.none()
    payment = payment_details.objects.none()
    order1 = order.objects.filter(buyer_id = username)
    
    for orderid in order1:
        payment = payment | payment_details.objects.filter(order_id = orderid.order_id)
        order_item1 = order_item1 | order_item.objects.filter(order_id = orderid.order_id)
    context = {
        'orders': order1,
        'order_item1': order_item1,
        'payment': payment,
    }
    
    return render(request , 'myorder.html',context)

def confirmation(request):
    print('in conf')
    cod = request.GET['cod']
    if cod == False:
        messages.info(request,'Please Complete Payment Process!')
        return redirect('checkout')
    else:
        return redirect('/')

def checkout(request):

    username = request.user.username  
    profile = profiles.objects.get(user_name= username) 
    cart = Cart.objects.filter(buyer_id = username)
    product_in_cart=[product for product in Cart.objects.all() if product.buyer_id==username]
    totalamount=0
    amount=0
    charge=0

    if product_in_cart:
        for product in product_in_cart:
            temp=(product.quantity*product.product.price)
            amount=temp+amount
            totalamount=amount+charge
    
    grand_total = totalamount + 70   

    if request.method == 'POST':
        try:
            cod = request.POST['cod']
        except:
            cod = False
        if cod == False:
            messages.info(request,'Please Complete Payment Process')
            return redirect('checkout')
        else: 
            
            temp_order_id = 0

            while True:  
                temp_order_id = random.randint(10000000, 99999999)  
                if not order.objects.filter(order_id= temp_order_id).exists():
                    break


            for prod in cart:
                product = prod.product
                product_quantity = prod.quantity
                order_id = temp_order_id

                an_order = order_item(product = product, product_quantity = product_quantity, order_id = order_id)
                an_order.save()
            
            payment = payment_details(order_id = temp_order_id, provider = "cod", amount = grand_total, status = "n")
            payment.save()

            main_order = order(order_id = temp_order_id, buyer_id = username, status = "pro", amount = grand_total)
            main_order.save()

            for prod in cart:
                prod.delete()
            
            messages.info(request,'Order Has Been Placed! Please go to My Orders for further details!')

            return render(request, 'sucess.html')

    context = {
        'carts':cart,
        'totalamount': totalamount,
        'profile': profile,
        'grandtotal': grand_total,
    }

    return render (request,'checkout.html',context)