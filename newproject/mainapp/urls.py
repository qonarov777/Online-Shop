from django.urls import path
from .views import IndexView
from .views import ShopView
from .views import DetailView
from .views import ContactView
from .views import CheckoutView
from .views import CartView

urlpatterns = [
    path('', IndexView, name='IndexView'),
    path('shop/', ShopView, name='ShopView'),
    path('detail/', DetailView, name='DetailView'),
    path('contact/', ContactView, name='ContactView'),
    path('checkout/',CheckoutView, name='CheckoutView'),
    path('cart/',CartView, name='CartView'),
    
]