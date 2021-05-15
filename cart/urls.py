from django.urls import path, include
from cart import views

urlpatterns = [
    path('cart1', views.cart1, name="cart1"),
    path('productdetail/<str:slug>', views.productdetail, name="productdetail"),
]
