from django.urls import path, include
from  orderapp import views

urlpatterns = [
    path('myorder/', views.myorder, name="myorder"),
    path('checkout/',views.checkout, name = "checkout"),
    path('esewa/', views.esewa, name="esewa"),
    path('confirmation/', views.confirmation, name="confirmation"),
]