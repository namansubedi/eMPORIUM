from django.urls import path, include
from home import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('upload', views.upload, name="upload" ),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('search', views.search, name="search"),
    path('profile', views.profile, name="profile"),
    path('editprofile', views.editprofile, name="editprofile"),
    path('faqs', views.faqs, name="faqs"),
    
    path('modify/<str:slug>', views.modify, name="modify"),
    path('password/', views.change_password, name='change_password'),
    path('category/<str:cat>', views.category, name="category"),


    #path('reset_password', auth_views.PasswordResetView.as_view(template_name = "password_reset.html"),name= "reset_password"),
    #path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    #path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),name=" password_reset_confirm"),
    #path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(),name=" password_reset_complete"),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
     
]
