from django.db import models
from home.models import products, profiles
from django.contrib.auth.models import User
# Create your models here.

status_CHOICES = (
    ("Processing", "Processing"),
    ("Delivering", "Delivering"),
    ("Delivered", "Delivered"),
    ("Cancelled", "Cancelled"),
)

class order(models.Model):
    order_id = models.BigIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    buyer_id = models.CharField(max_length=20)
    amount = models.FloatField()
    received_date = models.DateTimeField(auto_now=True)

class order_item(models.Model):
    order_id = models.BigIntegerField() 
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    product_quantity = models.IntegerField() #no. of this products in this order
    #added for fulfillment
    received_date = models.DateTimeField(auto_now=True)
    payment_detail = models.ForeignKey("orderapp.payment_details", on_delete=models.CASCADE)
    profile = models.ForeignKey(profiles, on_delete=models.CASCADE)
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    cost = models.FloatField()
    status = models.CharField(choices=status_CHOICES, max_length=10)

provider_CHOICES = (
    ("eSewa", "eSewa"),
    ("Cash On Delivery", "Cash On Delivery"),

)

payment_CHOICES = (
    ("Paid", "Paid"),
    ("Not Paid", "Not Paid"),

)

class payment_details(models.Model):
    order_id = models.BigIntegerField()
    provider = models.CharField(choices=provider_CHOICES, max_length=20)
    amount = models.FloatField() #total amount paid by the customer
    status = models.CharField(choices=payment_CHOICES, max_length=10)
    payment_date = models.DateTimeField(auto_now=True)
    seller_id = models.CharField(max_length=50)