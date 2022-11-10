from django.urls import path
from .views import IndexView
from .views import ShopView
from .views import DetailView
from .views import ContactView
from .views import CheckoutView
from .views import CartView

urlpatterns = [
    path('index/', IndexView),
    path('shop/', ShopView),
    path('detail/', DetailView),
    path('contact/', ContactView),
    path('checkout/',CheckoutView),
    path('cart/',CartView),
]