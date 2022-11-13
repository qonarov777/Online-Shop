from django.contrib import admin
from .models import shopnow
from .models import Featured, Categories

admin.site.register(shopnow)
admin.site.register(Featured)
admin.site.register(Categories)