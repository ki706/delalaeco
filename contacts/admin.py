from django.contrib import admin
from .models import ProductContact,ServiceContact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name','phone', 'email', 'car_title','car_id', 'city', 'create_date')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'email', 'car_title')
    list_per_page = 25

admin.site.register(ProductContact, ContactAdmin)




class ServiceContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name','phone', 'email', 'car_title','ser_id', 'city', 'create_date')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'email', 'car_title')
    list_per_page = 25

admin.site.register(ServiceContact, ServiceContactAdmin)