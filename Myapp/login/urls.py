from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.test,name='test'),
    path('loginuser/',views.loginuser, name='loginuser'),
    path('details/',views.details, name='details')
]
