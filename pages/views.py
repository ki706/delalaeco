from django.shortcuts import render, redirect
from .models import Team
 
from ads.models import Product, Service, ProductCatagory, ServiceCatagory
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.
def home(request):
    #featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Product.objects.order_by('-created').filter(is_verified=True)
    service = Service.objects.order_by('-created').filter(is_verified=True)
    pro_tag = ProductCatagory.objects.all()
    data = {
        'all_cars': all_cars,
        'service':service,
        'pro_tag' :pro_tag,
    }
    return render(request, 'pages/home.html', data)

 

def about(request):
    teams = Team.objects.all()
    data = {
        'teams' : teams,
    }
    return render(request, 'pages/about.html', data)

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = 'You have a new message from Carzone website regarding ' + subject
        message_body = 'Name: ' + name + '. Email: ' + email + '. Phone: ' + phone + '. Message: ' + message
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
                email_subject,
                message_body,
                'rathan.kumar049@gmail.com',
                [admin_email],
                fail_silently=False,
            )
        messages.success(request, 'Thank you for contacting us. We will get back to you shortly')
        return redirect('contact')
    
    return render(request, 'pages/contact.html')