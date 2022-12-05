from django.contrib import admin
from .models import Product, Service 
from django.utils.html import format_html


class ProductAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" height="40" style="border-radius: 50px;" />'.format(object.product_pics.url))
    
    thumbnail.short_description = 'Image'

    list_display = ( 'thumbnail', 'title', 'price', 'location', 'is_avilable', 'is_verified')
    list_display_links = ( 'thumbnail','title')
    #list_display = ('uuid', 'car_title')
    list_editable = ('is_verified','is_avilable')
    search_fields = ('uuid', 'title', 'discription' , 'location')
    list_filter = ('catagory','location', 'is_avilable', 'is_verified', 'created')


admin.site.register(Product, ProductAdmin)


class ServiceAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" height="40" style="border-radius: 50px;" />'.format(object.service_pics.url))
    
    thumbnail.short_description = 'Image'

    list_display = ( 'id','thumbnail', 'skill','title',  'location', 'experiance','is_avilable', 'is_verified')
    list_display_links = ( 'id','thumbnail','title')
    #list_display = ('uuid', 'car_title')
    list_editable = ('is_verified','is_avilable')
    search_fields = ('id', 'title', 'discription' , 'location')
    list_filter = ('catagory','location', 'is_avilable', 'is_verified', 'created','experiance')


admin.site.register(Service, ServiceAdmin)

 