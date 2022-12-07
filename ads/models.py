from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.shortcuts import reverse
import uuid
from PIL import Image 
import sys
from io import BytesIO
#from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files import File
#from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField 
from category.models import ProductCatagory,ServiceCatagory
from django.utils.translation import gettext_lazy as _
from PIL import Image, ImageDraw, ImageFont


location = (
        ('Addis Ababa', 'Addis Ababa'),
        ('Gondar', 'Gondar'),
        ('Dessie', 'Dessie'),
        ('Bahirdar', 'Bahirdar'),
        ('Semera', 'Semera'),
        
         
    )



class Product(models.Model):
   
    
    user = models.ForeignKey( settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name=_('user'))
    catagory = models.ForeignKey(ProductCatagory,on_delete=models.CASCADE,verbose_name=_('catagory'))
    title = models.CharField(max_length=50,verbose_name=_('title'))
    price = models.DecimalField(max_digits=10,decimal_places=2,verbose_name=_('price'))
    location = models.CharField(choices=location, max_length=100,verbose_name=_('location'))
    description = RichTextField(verbose_name=_('description'))
    is_avilable = models.BooleanField(default=True,verbose_name=_('is_avilable'))
    is_verified = models.BooleanField(default=False,verbose_name=_('is_verified'))
    product_pics = models.ImageField(upload_to='pro_pics/%Y/%m/%d/',verbose_name=_('product_picture'))
    product_pics1 = models.FileField(upload_to='pro_pics/%Y/%m/%d/',verbose_name=_('product_picture1'))
    #product_pics = CloudinaryField('image')
    created = models.DateTimeField (auto_now_add=True,verbose_name=_('created'))
    updated =models.DateTimeField(auto_now=True,verbose_name=_('updated'))
     
    class Meta:
        ordering =('-created',)
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        product_pics = Image.open(self.product_pics.path)
        draw = ImageDraw.Draw(product_pics)
        font = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf",30)
        width, height = product_pics.size
        myword = "Z-dealer.com"
        marigin = 10
        textwidth, textheight = draw.textsize(myword, font)
        x =width /2- textwidth/2     
        y = height/2 - textheight/2
        draw.text((x,y),myword,(255,255,255),font=font)
        product_pics.save(self.product_pics.path)
    def __str__(self):
        return self.title

           
 
    def get_absolute_url(self): # new
             return reverse('car_detail', args=[str(self.id)])
  
    
   

class Service(models.Model):
     
    user = models.ForeignKey( settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name=_('user'))
    catagory = models.ForeignKey(ServiceCatagory,on_delete=models.CASCADE,verbose_name=_('catagory'))
    title = models.CharField(max_length=50,verbose_name=_('title'))
    skill = models.CharField(max_length=1000,verbose_name=_('skill'))
    experiance = models.PositiveSmallIntegerField(verbose_name=_('experiance'))
    # price = models.DecimalField(max_digits=10,decimal_places=2)
    location = models.CharField(choices=location, max_length=100,verbose_name=_('location'))
    description = RichTextField(verbose_name=_('description'))
    is_avilable = models.BooleanField(default=True,verbose_name=_('is_avilable'))
    is_verified = models.BooleanField(default=False,verbose_name=_('is_verified'))
    service_pics = models.ImageField(upload_to='pro_pics/%Y/%m/%d/',verbose_name=_('service_picture'))
    service_pics1 = models.FileField(upload_to='pro_pics/%Y/%m/%d/',verbose_name=_('service_picture'))
    #product_pics = CloudinaryField('image')
     
    created = models.DateTimeField (auto_now_add=True,verbose_name=_('created'))
    updated =models.DateTimeField(auto_now=True,verbose_name=_('updated'))
     
    class Meta:
        ordering =('-created',)
        verbose_name = _('Human Resource')
        verbose_name_plural = _('Human Resources')
    def __str__(self):
        return self.title

       
 
    def get_absolute_url(self): # new
             return reverse('ser_detail', args=[str(self.skill)])
  
    
  
           
 
 