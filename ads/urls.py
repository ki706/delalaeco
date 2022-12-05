from django.urls import path
from . import views
from .views import ServiceCreationView,ProductCreationView

urlpatterns = [
    path('', views.cars, name='ads'),
    path('p/<int:id>', views.car_detail, name='car_detail'),
    path('s/<int:id>', views.ser_detail, name='ser_detail'),

    path('post',views.ads_creation, name= 'ads_creation'),
    path('post/service',ServiceCreationView.as_view(), name = 'service_form'),
    path('post/product',ProductCreationView.as_view(), name = 'pro_form'),
    path('search', views.search, name='search'),
]