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

