from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(order)
admin.site.register(order_item)
admin.site.register(payment_details)