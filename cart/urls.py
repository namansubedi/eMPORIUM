from django.urls import path, include
from cart import views

urlpatterns = [
    path('addtocart/', views.addtocart, name="addtocart"),
    path('productdetail/<str:slug>', views.productdetail, name="productdetail"),
    path('showcart/', views.showcart, name="showcart"),
    path('delete/<int:id>', views.delete, name="delete"),
   
]
