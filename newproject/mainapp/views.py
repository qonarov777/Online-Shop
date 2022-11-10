from django.shortcuts import render

def IndexView(request):
    return render(request, 'index.html')

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