from django.contrib import admin
from .models import CustomUser
# Register your models here.


@admin.register(CustomUser)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','phone_number']