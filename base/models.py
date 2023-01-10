from django.db import models

# Create your models here.
class Product(models.Model):
    desc = models.CharField(max_length=50,null=True,blank=True)
    image = models.ImageField(null=True,blank=True,default='/placeholder.png')
    price = models.DecimalField(max_digits=5,decimal_places=2)
 
    def __str__(self):
           return self.desc
