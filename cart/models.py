from django.db import models

# Create your models here.
class Cart(models.Model):
    buyer_id = models.CharField(max_length=50)
    product_id = models.IntegerField()
    quantity = models.IntegerField()
