from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('upload', views.upload, name="upload" ),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
]
