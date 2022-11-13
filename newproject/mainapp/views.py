from django.shortcuts import render
from .models import shopnow,  Categorie




def IndexView(request):
    
    Shopnow = shopnow.objects.all()
    
    categ= Categorie.objects.all()
    
    context={
                'Shopnow':Shopnow,
                'categ': categ,
                }
    
    return render(request, 'index.html', context=context)





def SopView(request):
    return render(request, 'shop.html')

def DetailView(request):
    return render(request, 'detail.html')

def ContactView(request):
    return render(request, 'contact.html')

def CheckoutView(request):
    return render(request, 'checkout.html')

def CartView(request):
    return render(request, 'cart.html')