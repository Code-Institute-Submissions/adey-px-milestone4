from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('upgrade', views.upgrade, name='upgrade'),
    path('checkout', views.checkout, name='checkout'),
]
