from django.urls import path
from .import views
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns=[

    path('',views.store,name="store"),
    path('register/',views.register,name="register"),
    
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),
    path('update_item/',views.updateItem,name="update_item"),
    path('process_order/',views.processOrder,name="process_order")

]