from django.db import models

# Create your models here.
class profiles(models.Model):
    user_name = models.CharField(max_length=50)
    phone_number = models.BigIntegerField()
    region = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    area = models.CharField(max_length=15)
    locale = models.CharField(max_length=50)
    is_seller = models.BooleanField(default=False)
    gmap = models.CharField(max_length=100, blank=True, null=True)

category_CHOICES = (
    ("elec", "electronic"),
    ("lap", "laptops"),

)

class products(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(choices=category_CHOICES ,max_length=5)
    slug = models.SlugField(max_length=50, unique=True)
    price = models.IntegerField()
    brand = models.CharField(max_length=50)
    seller_id = models.CharField(max_length=50)
    image = models.ImageField(upload_to='product_pics')
    description = models.TextField()
    stock = models.PositiveIntegerField()
    keywords = models.TextField()
    detail = models.TextField(blank=True, null=True)

class Feedback(models.Model):
    user_id = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    text = models.TextField()