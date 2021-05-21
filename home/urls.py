from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('upload', views.upload, name="upload" ),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('search', views.search, name="search"),
    path('profile', views.profile, name="profile"),
    path('editprofile', views.editprofile, name="editprofile"),
    path('myproducts', views.myproducts, name="myproducts"),
    path('modify/<str:slug>', views.modify, name="modify")
]
