from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/service/<int:id>', views.scategory, name='scategory'),
    path('category/product/<int:id>', views.pcategory, name='pcategory'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
]