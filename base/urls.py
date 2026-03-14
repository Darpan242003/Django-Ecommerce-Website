from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_product', views.add_product, name='add_product'),
    path('cart', views.cart, name='cart'),
    path('addtocart/<int:pk>', views.addtocart, name='addtocart'),
    path('removefromcart/<int:pk>', views.removefromcart, name='removefromcart'),
]
