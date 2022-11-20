from django.shortcuts import render
from .models import shopnow,  Categorie, Collection, Products, Arrived, Vendorr, Link, Shopproduct


def IndexView(request):
    
    Shopnow = shopnow.objects.all()
    
    categ= Categorie.objects.all()
    collection=Collection.objects.all()
    product=Products.objects.all()
    arrived=Arrived.objects.all()
    vonder=Vendorr.objects.all()
    link=Link.objects.all().first()
    context={
                'Shopnow':Shopnow,
                'categ': categ,
                'collection': collection,
                'product':product,
                'arrived':arrived,
                'vonder':vonder,
                'link':link
                }
    
    return render(request, 'index.html', context=context)


def ShopView(request):
    products=Shopproduct.objects.all()
    
    context={
        'products':products,
                }
    return render(request, 'shop.html', context=context)

def DetailView(request):
    return render(request, 'detail.html')

def ContactView(request):
    return render(request, 'contact.html')

def CheckoutView(request):
    return render(request, 'checkout.html')

def CartView(request):
    return render(request, 'cart.html')