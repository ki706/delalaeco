from django.urls import path
from . import views

urlpatterns = [
    path('sinquiry', views.sinquiry, name='sinquiry'),
    path('pinquiry', views.pinquiry, name='pinquiry'),
] 