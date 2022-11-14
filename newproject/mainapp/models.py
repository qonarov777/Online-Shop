from django.db import models

CATEGORIES=(
                ('Fashionable Dress','Fashionable Dress'),
                ('Reasonable Price','Reasonable Price')
                )
class shopnow(models.Model):
    title=models.CharField(max_length=50)
    categories=models.CharField(max_length=50, choices=CATEGORIES)
    image=models.ImageField(upload_to='media/shopnow/')
    
    def __str__(self):
        return self.categories
    
    class Meta:
        verbose_name='Basic view'
        verbose_name_plural='Basic views'
    
    
class Categorie(models.Model):
    title=models.CharField( max_length=50)
    image= models.ImageField(upload_to="media/Categories/")
    number = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Categorie'
        verbose_name_plural='Categories'
        
class Collection(models.Model):
    title=models.CharField( max_length=50)
    season=models.CharField(max_length=50)
    image=models.ImageField( upload_to='media/Collecton/', height_field=None, width_field=None, max_length=None)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Collection'
        verbose_name_plural='Collections'
        
class Products(models.Model):
    image= models.ImageField( upload_to=None)
    title=models.CharField( max_length=50)
    cost= models.IntegerField()
    cost_delate= models.IntegerField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Product'
        verbose_name_plural='Products'
    
class Arrived(models.Model):
    image= models.ImageField( upload_to=None)
    title=models.CharField( max_length=50)
    cost= models.IntegerField()
    cost_delate= models.IntegerField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Product arrived'
        verbose_name_plural='Products arrived'
        
class Vendorr(models.Model):
    image= models.ImageField(upload_to='media/Vendor')   
    
    class Meta:
        verbose_name='Vendor'
        verbose_name_plural='Vendors'     

class Link(models.Model):
    facebook=models.CharField(max_length=50)
    twitter= models.CharField(max_length=50)
    linkland=models.CharField( max_length=50)
    instagram=models.CharField(max_length=50)
    youtobe=models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    number=models.IntegerField()
    location=models.CharField(max_length=50)
    
    def __str__(self):
        return self.instagram
    
    class Meta:
        verbose_name='link'
        verbose_name_plural='links'   
    
    