from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ProductContact, ServiceContact
from accounts.models import CustomUser
from django.contrib.auth.models import User
from django.core.mail import send_mail
from ads.models import Product, Service
# Create your views here.


def pinquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = ProductContact.objects.all().filter(car_id=car_id, user_id = user_id)
            has_inquiried = Product.objects.filter(id=car_id, user_id = user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry about this car. Please wait until we get back to you.')
                return redirect('/ads/p/'+car_id)

            if has_inquiried:
                messages.error(request, 'You Can not  inquiry Your Car.')
                return redirect('/ads/p/'+car_id)    



    contact = ProductContact(car_id=car_id, car_title=car_title, user_id=user_id,
        first_name=first_name, last_name=last_name, customer_need=customer_need, city=city,
        email=email, phone=phone, message=message)
     
    contact.save()
    messages.success(request, 'Your request has been submitted, we will get back to you shortly.')
    return redirect('/ads/p/'+car_id)





def sinquiry(request):
    if request.method == 'POST':
        ser_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = ServiceContact.objects.all().filter(ser_id=ser_id, user_id = user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry about this car. Please wait until we get back to you.')
                return redirect('/ads/s/'+car_id)
            print('idddd'+ ser_id)
            ser_id = int(ser_id)
    contact = ServiceContact(ser_id=ser_id, car_title=car_title, user_id=user_id,
        first_name=first_name, last_name=last_name, customer_need=customer_need, city=city,
        email=email, phone=phone, message=message)
    """
    admin_info = CustomUser.objects.get(is_superuser=True)
    admin_email = admin_info.email
    send_mail(
                'New Car Inquiry',
                'You have a new inquiry for the car ' + car_title + '. Please login to your admin panel for more info.',
                'arunakampati@gmail.com',
                [admin_email],
                fail_silently=False,
            )
     """
    contact.save()
    messages.success(request, 'Your request has been submitted, we will get back to you shortly.')
    return redirect('/ads/s/'+car_id)
