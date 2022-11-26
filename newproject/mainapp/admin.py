from django.contrib import admin
from .models import shopnow
from .models import  Categorie,Collection, Products, Arrived,Vendorr,Link,Shopproduct,Shopdetails

admin.site.register(shopnow)
admin.site.register(Categorie)
admin.site.register(Collection)
admin.site.register(Products)
admin.site.register(Arrived)
admin.site.register(Vendorr)
admin.site.register(Link)
admin.site.register(Shopproduct)
admin.site.register(Shopdetails)