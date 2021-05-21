from django.urls import path, include
from  orderapp import views

urlpatterns = [
    path('order/', views.order, name="order"),
    path('checkout/',views.checkout, name = "checkout")
]