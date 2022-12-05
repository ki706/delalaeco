from django.db import models
from datetime import datetime
from ads.models import Service
# Create your models here.
from django.utils.translation import gettext_lazy as _

class ProductContact(models.Model):
    first_name = models.CharField(max_length=100,verbose_name=_('firs tname'))
    last_name = models.CharField(max_length=100,verbose_name=_('last name'))
    car_id = models.IntegerField(verbose_name=_('product id'))
    customer_need = models.CharField(max_length=100,verbose_name=_('customer need'))
    car_title = models.CharField(max_length=100,verbose_name=_('car title'))
    city = models.CharField(max_length=100,verbose_name=_('city'))
    email = models.EmailField(max_length=100,verbose_name=_('email'))
    phone = models.CharField(max_length=100,verbose_name=_('phone number'))
    message = models.TextField(blank=True,verbose_name=_('message'))
    user_id = models.IntegerField(blank=True,verbose_name=_('user id'))
    create_date = models.DateTimeField(blank=True, default=datetime.now,verbose_name=_('created date'))
    

    class Meta:
        verbose_name = _('Product Contact')
        verbose_name_plural = _('Product Contacts')
    def __str__(self):
        return self.email



class ServiceContact(models.Model):
    first_name = models.CharField(max_length=100,verbose_name=_('firs tname'))
    last_name = models.CharField(max_length=100,verbose_name=_('last name'))
    car_id = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name=_('human resource id'))
    customer_need = models.CharField(max_length=100,verbose_name=_('customer need'))
    car_title = models.CharField(max_length=100,verbose_name=_('service title'))
    city = models.CharField(max_length=100,verbose_name=_('city'))
    email = models.EmailField(max_length=100,verbose_name=_('email'))
    phone = models.CharField(max_length=100,verbose_name=_('phone number'))
    message = models.TextField(blank=True,verbose_name=_('message'))
    user_id = models.IntegerField(blank=True,verbose_name=_('user id'))
    create_date = models.DateTimeField(blank=True, default=datetime.now,verbose_name=_('created date'))
    

    class Meta:
        verbose_name = _('Human Resource Contact')
        verbose_name_plural = _('Human Resource Contacts')

    def __str__(self):
        return self.email
