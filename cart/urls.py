from django.urls import path, include
from cart import views

urlpatterns = [
    path('addtocart/', views.addtocart, name="addtocart"),
     path('addtocarts/<str:slug>', views.addtocarts, name="addtocarts"),
    path('productdetail/<str:slug>', views.productdetail, name="productdetail"),
    path('showcart/', views.showcart, name="showcart"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('buynow/<str:slug>', views.buynow, name="buynow"),
    path('pluscart/', views.pluscart,name="pluscart"),
    path('minuscart/', views.minuscart,name="minuscart"),
    path('deletecart/<str:slug>', views.deletecart,name="deletecart"),
   
   
]
