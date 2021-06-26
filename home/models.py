from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class profiles(models.Model):
    user_name = models.CharField(max_length=50)
    phone_number = models.BigIntegerField()
    region = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    area = models.CharField(max_length=15)
    locale = models.CharField(max_length=50)
    is_seller = models.BooleanField(default=False, verbose_name = 'Do you want to sell with eMPORIUM?')
    gmap = models.CharField(max_length=100, blank=True, null=True)
    pan = models.BigIntegerField()
    
    
    def __str__(self):
        return str(self.user_name)


category_CHOICES = (
    ("General Electronics", "General Electronics"),
    ("Electronics-Smartphones", "Electronics-Smartphones"),
    ("Electronics-PC's", "Electronics-PC's"),
    ("Electronics-PC Components", "Electronics-PC Components"),
    ("Electronics-Laptops", "Electronics-Laptops"),
    ("Fashion-Mens", "Fashion-Mens"),
    ("Fashion-Womens", "Fashion-Womens"),
    ("Fashion-Unisex", "Fashion-Unisex"),
    ("Fashion-Shoes", "Fashion-Shoes"),

)

class products(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(choices=category_CHOICES ,max_length=50)
    slug = AutoSlugField(populate_from='name')
    price = models.IntegerField()
    brand = models.CharField(max_length=50)
    seller_id = models.CharField(max_length=50)
    image = models.ImageField(upload_to='product_pics')
    description = models.TextField()
    stock = models.IntegerField(default=0)
    keywords = models.TextField()
    detail = models.TextField(blank=True, null=True)
    available_offer = models.TextField(default="No offer available.")
    
    def get_url(self):
        return reverse('productdetail', args=[self.slug])

   

    
    
    
    def __str__(self):
        return str(self.name)


    def slugify_function(self, content):
        return content.replace(' ', '-').lower()
    

class Feedback(models.Model):
    
    email = models.CharField(max_length=100)
    text = models.TextField()
    created_time =models.DateTimeField(auto_now_add=True)
    
    
   
