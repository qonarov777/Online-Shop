from django.shortcuts import render
from .models import shopnow, Featured, Categories
from django.db.models import Q  



def IndexView(request):
    
    search_post = request.GET.get('search')
    print(search_post, 'kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
    if search_post:
        Shopnow = shopnow.objects.filter(Q(title = search_post) | Q(categories = search_post))
    else:
        Shopnow = shopnow.objects.all()
    Shopnow = shopnow.objects.all()
    
    
    featured= Featured.objects.all()
    categoriess= Categories.objects.all()
    ifid = shopnow.objects.last()
    
    print(ifid.title)
    
    context={
                'Shopnow':Shopnow,
                'featured': featured,
                'categoriess': categoriess,
                'ifid' : ifid
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