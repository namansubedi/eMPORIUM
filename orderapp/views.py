from django.shortcuts import render, redirect
from cart.models import Cart
from orderapp.models import order, payment_details, order_item
from home.models import profiles
from django.contrib import messages
import random
from .forms import fulfillform, paymentform

def fulfillmentdetails(request, id):
    user = request.user
    username = user.username
    if request.method == 'POST':
        id = request.POST['id']
        form1 = fulfillform(request.POST)
        if form1.is_valid():
            status1 = form1.cleaned_data['status']
            paystat = request.POST['pay']
            item1 = order_item.objects.filter(order_id=id) & order_item.objects.filter(product__seller_id = username)
            p = payment_details.objects.filter(seller_id=username)
            for i in item1:   
                prod = i.product          
                i.status=status1
                if status1 == "Cancelled":          #to increase stock of product if the order is cancelled by vendor
                    prod.stock += 1
                    prod.save()
                i.save()
            for pa in p:
                pa.status = paystat
                pa.save()
            return redirect('fulfillment')
        else:
            print(1)
        return redirect('fulfillment')
    else:
        send_items = order_item.objects.filter(order_id = id) & order_item.objects.filter(product__seller_id = username)
        context = {
            'order_items': send_items,
            'address': send_items[0].profile,
            'form1': fulfillform,
            'id': id,
        }
        return render(request, 'fulfillmentdetails.html', context)

def fulfillment(request):

    user = request.user
    username = user.username
    id_list = []
    no_sold = 0
    send_orders = order_item.objects.none()
    all_orders = order_item.objects.all()
    order1 = order.objects.all()
    order2 = order.objects.none()
    for item in all_orders:
        no_sold += 1
        if item.product.seller_id == username:
            #send_orders = send_orders | item
            id = item.order_id
            id_list.append(id)
    #print(send_orders)
    #print(id_list)
    id_finallist = [i for j, i in enumerate(id_list) if i not in id_list[:j]] 

    #for o in order1:
        #for ide in id_finallist:
            #if o.order_id == ide:
                #order2 = order2 | o
                #print(order2)

    send_orders = order_item.objects.filter(product__seller_id=username)
    context = {
        'order_items': send_orders,
        'id_list': id_finallist,
        'no_sold': no_sold,
    }
    return render(request, 'fulfillment.html', context)

def orderdetails(request, orderid):
    order1 = order.objects.get(order_id = orderid)
    orderitem = order_item.objects.filter(order_id =  orderid)
    context = {
        'orders': order1,
        'orderitem': orderitem,
    }
    return render(request, 'orderdetails.html', context)

def esewa(request):
    pass

def myorder(request):
    username = request.user.username  
    order_item1 =  order_item.objects.none()
    payment = payment_details.objects.none()
    order1 = order.objects.filter(buyer_id = username).order_by('id').reverse()
    
    for orderid in order1:
        payment = payment | payment_details.objects.filter(order_id = orderid.order_id)
        order_item1 = order_item1 | order_item.objects.filter(order_id = orderid.order_id)
    context = {
        'orders': order1,
        'order_item1': order_item1,
        'payment': payment,
    }
    
    return render(request , 'myorder.html',context)

def checkout(request):

    user = request.user
    username = user.username  
    profile = profiles.objects.get(user_name= username) 
    cart = Cart.objects.filter(buyer_id = username)
    product_in_cart=[product for product in Cart.objects.all() if product.buyer_id==username]
    totalamount=0
    amount=0
    charge=0
    no_of_items=0

    if product_in_cart:
        no_of_items += 1
        
        for product in product_in_cart:
            if product.quantity==0:
                return redirect('deletecart',slug=product.product.slug)
                
            
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
                payment = payment_details(order_id = temp_order_id, provider = "Cash On Delivery", amount = grand_total, status = "Not Paid", seller_id=prod.product.seller_id)
                product = prod.product
                product_quantity = prod.quantity
                order_id = temp_order_id
                #print(product.stock)
                product.stock -= product_quantity
                #print(product.stock)
                product.save()
                payment.save()
                an_order = order_item(product = product, product_quantity = product_quantity, order_id = order_id, payment_detail = payment, profile=profile, buyer=user, cost = product.price, status="Processing")
                an_order.save()

            main_order = order(order_id = temp_order_id, buyer_id = username, amount = grand_total)
            main_order.save()

            for prod in cart:
                prod.delete()
            return render(request, 'sucess.html')

    context = {
        'carts':cart,
        'totalamount': totalamount,
        'profile': profile,
        'grandtotal': grand_total,
    }

    return render (request,'checkout.html',context)