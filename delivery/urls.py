from django.urls import path
from . import views

urlpatterns = [
    path('delivery_form', views.delivery_form, name='delivery_form'),
    path('order_placed', views.delivery_form, name='order_placed'),
]
