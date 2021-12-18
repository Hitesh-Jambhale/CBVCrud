from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', user_register_view, name='registerpage'),
    path('login/', login_view,
         name='loginpage'),
    path('logout/', logout_view, name='logout')
]
