from django.db import models
from django.contrib.auth.models import User
from home .models import *
# Create your models here.
class Cart(models.Model):
    buyer_id = models.CharField(max_length=50)
    product=models.ForeignKey(products,on_delete=models.CASCADE,null=True)
    quantity = models.PositiveIntegerField(default=1)
    
    
    def __str__(self):
        return self.buyer_id
    
    
    
 


