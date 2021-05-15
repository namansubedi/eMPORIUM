from django.db import models
from django_extensions.db.fields import AutoSlugField

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
    ("el01", "General Electronics"),
    ("el02", "Electronics-Smartphones"),
    ("el03", "Electronics-PC's"),
    ("el04", "Electronics-PC Components"),
    ("el05", "Electronics-Laptops"),
    ("fs01", "Fashion-Mens"),
    ("fs02", "Fashion-Womens"),
    ("fs03", "Fashion-Unisex"),
    ("fs04", "Fashion-Shoes"),

)

class products(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(choices=category_CHOICES ,max_length=5)
    slug = AutoSlugField(populate_from='name')
    price = models.IntegerField()
    brand = models.CharField(max_length=50)
    seller_id = models.CharField(max_length=50)
    image = models.ImageField(upload_to='product_pics')
    description = models.TextField()
    stock = models.PositiveIntegerField()
    keywords = models.TextField()
    detail = models.TextField(blank=True, null=True)

    def slugify_function(self, content):
        return content.replace('_', '-').lower()

class Feedback(models.Model):
    user_id = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    text = models.TextField()