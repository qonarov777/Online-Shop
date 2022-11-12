from django.shortcuts import render
from .models import shopnow

def IndexView(request):
    
    Shopnow = shopnow.objects.all()
    context={
                'Shopnow':Shopnow
                }
    
    return render(request, 'index.html', context=context)

def ShopView(request):
    return render(request, 'shop.html')

def DetailView(request):
    return render(request, 'detail.html')

def ContactView(request):
    return render(request, 'contact.html')

def CheckoutView(request):
    return render(request, 'checkout.html')

def CartView(request):
    return render(request, 'cart.html')