from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import ProductContact
from ads.models import Product, Service
from django.contrib.auth.decorators import login_required
# Create your views here.
def logon(request):
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        user = auth.authenticate(phone_number=phone_number, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid login credentials')
            return redirect('logon')
    return render(request, 'accounts/logon.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists!')
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email, username=username, password=password)
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in.')
                    return redirect('dashboard')
                    user.save()
                    messages.success(request, 'You are registered successfully.')
                    return redirect('login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

@login_required(login_url= 'account_login')
def dashboard(request):
    user_pinquiry = ProductContact.objects.order_by('-create_date').filter(user_id = request.user.id)
    user_ppost  = Product.objects.order_by('-created').filter(user_id = request.user.id)  
    user_spost = Service.objects.order_by('-created').filter(user_id = request.user.id)

    combined = list(user_ppost) + list(user_spost)
    data = {
        'inquires' : user_pinquiry,
        'combined' :combined,
        'user_ppost':user_ppost,
        'user_spost': user_spost,
    }
    return render(request, 'accounts/dashboard.html', data)

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return redirect('home')

