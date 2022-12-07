from django.db import models

# Create your models here.
from django.utils.translation import gettext_lazy as _

class ProductCatagory(models.Model):
    catagory = models.CharField(max_length=70,verbose_name=_('catagory'))
    catagory_image = models.ImageField(upload_to='category_pic/%Y/%m/%d/',verbose_name=_('category_picture'))
    
    class Meta:
        verbose_name = _('Product Category')
        verbose_name_plural = _('Products Category')

    def __str__(self):
        return self.catagory

class ServiceCatagory(models.Model):
    catagory = models.CharField(max_length=70,verbose_name=_('catagory'))
    catagory_image = models.ImageField(upload_to='category_pic/%Y/%m/%d/',verbose_name=_('category_picture'))
    class Meta:
        verbose_name = _('Human Resource Category')
        verbose_name_plural = _('Human Resources Categories')

    def __str__(self):
        return self.catagory
 