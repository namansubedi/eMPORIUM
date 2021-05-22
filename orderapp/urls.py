from django.urls import path, include
from  orderapp import views

urlpatterns = [
    path('myorder/', views.myorder, name="myorder"),
    path('checkout/',views.checkout, name = "checkout"),
    path('orderdetails/<int:orderid>', views.orderdetails, name="orderdetails"),
    path('esewa/', views.esewa, name="esewa"),
    path('confirmation/', views.confirmation, name="confirmation"),
]