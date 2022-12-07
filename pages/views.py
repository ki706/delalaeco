from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Team
from category.models import ProductCatagory,ServiceCatagory 
from ads.models import Product, Service, ProductCatagory, ServiceCatagory
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
# Create your views here.
def home(request):
    #featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Product.objects.order_by('-created').filter(is_verified=True)[:10]
    service = Service.objects.order_by('-created').filter(is_verified=True)[:10]
    pro_tag = ProductCatagory.objects.all()
    ser_tag = ServiceCatagory.objects.all()
    combined_tag = list(pro_tag) + list(ser_tag)
    data = {
        'all_cars': all_cars,
        'service':service,
        'pro_tag' : pro_tag,
        'ser_tag' :ser_tag,
    }
    return render(request, 'pages/home.html', data)

 
def pcategory(request, id):
    
    get_pro_cat = get_object_or_404(ProductCatagory, pk=id)
    pro_cat =  Product.objects.filter(catagory=get_pro_cat.id)
    paginator = Paginator(pro_cat, 5)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    
    data = {
       
        'pro_cat' :paged_cars,
         
        
    }    
    return render(request, 'pages/catagories.html', data)

def scategory(request, id):
    get_ser_cat = get_object_or_404(ServiceCatagory, pk=id)
    ser_cat =  Service.objects.filter(catagory=get_ser_cat.id)
    paginator = Paginator(ser_cat, 5)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    data = {
        'ser_cat' : paged_cars,
        
         
        
    }    
    return render(request, 'pages/catagories.html', data)


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
        """ admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
                email_subject,
                message_body,
                'rathan.kumar049@gmail.com',
                [admin_email],
                fail_silently=False,
            )  """
        messages.success(request, 'Thank you for contacting us. We will get back to you shortly')
        return redirect('contact')
    
    return render(request, 'pages/contact.html')