from django.db import models
from home.models import products
# Create your models here.

status_CHOICES = (
    ("pro", "Processing"),
    ("del", "Delivering"),

)

class order(models.Model):
    order_id = models.BigIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    buyer_id = models.CharField(max_length=20)
    status = models.CharField(choices=status_CHOICES, max_length=10)
    amount = models.FloatField()
    received_date = models.DateTimeField(auto_now_add=True)

class order_item(models.Model):
    order_id = models.BigIntegerField() 
    product = models.ForeignKey(products, on_delete=models.CASCADE)
    product_quantity = models.IntegerField() #no. of this products in this order

provider_CHOICES = (
    ("e", "eSewa"),
    ("cod", "Cash On Delivery"),

)

payment_CHOICES = (
    ("y", "Paid"),
    ("n", "Not Paid"),

)

class payment_details(models.Model):
    order_id = models.BigIntegerField()
    provider = models.CharField(choices=provider_CHOICES, max_length=10)
    amount = models.FloatField() #total amount paid by the customer
    status = models.CharField(choices=payment_CHOICES, max_length=10)
    payment_date = models.DateTimeField(auto_now_add=True)