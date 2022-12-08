from django.db import models
from datetime import datetime
from ads.models import Service,Product
# Create your models here.
import requests
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import truncatechars


class ProductContact(models.Model):
    first_name = models.CharField(max_length=100,verbose_name=_('firs tname'))
    last_name = models.CharField(max_length=100,verbose_name=_('last name'))
    car_id = models.ForeignKey(Product,on_delete=models.CASCADE, verbose_name=_('product id'))
    customer_need = models.CharField(max_length=100,verbose_name=_('customer need'))
    car_title = models.CharField(max_length=100,verbose_name=_('car title'))
    city = models.CharField(max_length=100,verbose_name=_('city'))
    email = models.EmailField(max_length=100,verbose_name=_('email'))
    phone = models.CharField(max_length=100,verbose_name=_('phone number'))
    message = models.TextField(blank=True,verbose_name=_('message'))
    user_id = models.IntegerField(blank=True,verbose_name=_('user id'))
    message_to_customer = models.TextField(verbose_name=_('message to customer'),null=True,blank=True)
    create_date = models.DateTimeField(blank=True, default=datetime.now,verbose_name=_('created date'))
    

    class Meta:
        verbose_name = _('Product Contact')
        verbose_name_plural = _('Product Contacts')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        session = requests.Session()
        base_url = 'https://api.afromessage.com/api/send'
        token = 'eyJhbGciOiJIUzI1NiJ9.eyJpZGVudGlmaWVyIjoicUZlU2ZwazJiMGlHdHZUTzMzQ0Z2WlhFYXBtc0poeGEiLCJleHAiOjE4MjgxMDI3MzYsImlhdCI6MTY3MDMzNjMzNiwianRpIjoiZWEyNzUwODItN2U5Ny00ZTEyLWE3YTMtYjFkYzk3MGExNGJlIn0.L1s6Q5mtUcCVidXukHhXnGneNAe3lADpEsyQ6fXr2ZI'
        headers = {'Authorization': 'Bearer ' + token}
        body = {'callback': '',
            'from':'',   # 9786
            'sender':'',   #
            'to':self.phone,
            'message': self.message_to_customer}
        #print(body)
        result = session.post(base_url, json=body, headers=headers) 
    @property
    def message_to_customr1(self):
        verbose_name = _('message_to_customer')
        return truncatechars(self.message_to_customer, 15)    
    def __str__(self):
        return self.first_name



class ServiceContact(models.Model):
    first_name = models.CharField(max_length=100,verbose_name=_('firs tname'))
    last_name = models.CharField(max_length=100,verbose_name=_('last name'))
    ser_id = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name=_('human resource id'))
    customer_need = models.CharField(max_length=100,verbose_name=_('customer need'))
    car_title = models.CharField(max_length=100,verbose_name=_('service title'))
    city = models.CharField(max_length=100,verbose_name=_('city'))
    email = models.EmailField(max_length=100,verbose_name=_('email'))
    phone = models.CharField(max_length=100,verbose_name=_('phone number'))
    message = models.TextField(blank=True,verbose_name=_('message'))
    user_id = models.IntegerField(blank=True,verbose_name=_('user id'))
    message_to_customer = models.TextField(verbose_name=_('message to customer'),null=True,blank=True)
    create_date = models.DateTimeField(blank=True, default=datetime.now,verbose_name=_('created date'))
    

    class Meta:
        verbose_name = _('Human Resource Contact')
        verbose_name_plural = _('Human Resource Contacts')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        session = requests.Session()
        base_url = 'https://api.afromessage.com/api/send'
        token = 'eyJhbGciOiJIUzI1NiJ9.eyJpZGVudGlmaWVyIjoicUZlU2ZwazJiMGlHdHZUTzMzQ0Z2WlhFYXBtc0poeGEiLCJleHAiOjE4MjgxMDI3MzYsImlhdCI6MTY3MDMzNjMzNiwianRpIjoiZWEyNzUwODItN2U5Ny00ZTEyLWE3YTMtYjFkYzk3MGExNGJlIn0.L1s6Q5mtUcCVidXukHhXnGneNAe3lADpEsyQ6fXr2ZI'
        headers = {'Authorization': 'Bearer ' + token}
        body = {'callback': '',
            'from':'',   # 9786
            'sender':'',   #
            'to':self.phone,
            'message': self.message_to_customer}
        #print(body)
        result = session.post(base_url, json=body, headers=headers)     
    @property
    def message_to_customr1(self):
        verbose_name = _('message_to_customer')
        return truncatechars(self.message_to_customer, 15)
    def __str__(self):
        return self.first_name 
