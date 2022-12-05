from django.contrib import admin

# Register your models here.

from .models import ProductCatagory, ServiceCatagory


admin.site.register(ProductCatagory)
admin.site.register(ServiceCatagory)
