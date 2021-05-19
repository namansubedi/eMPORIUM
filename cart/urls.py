from django.urls import path, include
from cart import views

urlpatterns = [
    path('addtocart/', views.addtocart, name="addtocart"),
    path('productdetail/<str:slug>', views.productdetail, name="productdetail"),
    path('showcart/', views.showcart, name="showcart"),
   
]
