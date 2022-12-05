from django.shortcuts import render, get_object_or_404
from .models import Product, Service, ProductCatagory, ServiceCatagory
from .forms import ServiceCreationForm, ProductCreationForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from taggit.models import Tag
# Create your views here.
def cars(request):
    cars = Product.objects.order_by('-created').filter(is_verified=True)
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    pro_tag = ProductCatagory.objects.all()
    city_search = Product.objects.values_list('location', flat=True).distinct()
    
    data = {
        'cars' : paged_cars,
        'pro_tag' :pro_tag,
        'city_search': city_search,
        
    }
    return render(request, 'ads/ads.html', data)

def ads_creation(request):
    pro_cat = ProductCatagory.objects.all()
    ser_cat = ServiceCatagory.objects.all()
    data = {
         
        'pro_cat' :pro_cat,
        'ser_cat' :ser_cat,
        
    }
    return render(request, 'ads/ads_creation.html',data)

class ServiceCreationView(LoginRequiredMixin,CreateView):
    model = Service
    form_class = ServiceCreationForm
    success_url = reverse_lazy ('home')
    template_name = 'ads/service_forms.html'
    def form_valid(self,form ):
        form.instance.user = self.request.user 
        """ file = request.data.get('product_pics')
        #cloudinary.uploader.upload(file)  
        cloudinary.uploader.upload(request.FILES['file']) """
        #cloudinary.uploader.upload(Product.product_pics)
        response= super().form_valid(form) 
        
        return response



class ProductCreationView(LoginRequiredMixin,CreateView):
    model = Product
    form_class = ProductCreationForm
    success_url = reverse_lazy ('home')
    template_name = 'ads/pro_form.html'
    def form_valid(self,form ):
        form.instance.user = self.request.user 
        """ file = request.data.get('product_pics')
        #cloudinary.uploader.upload(file)  
        cloudinary.uploader.upload(request.FILES['file']) """
        #cloudinary.uploader.upload(Product.product_pics)
        response= super().form_valid(form) 
        
        return response       
    """
    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('service_pics')
        if form.is_valid():
            for f in files:
                ff = cloudinary.uploader.upload(request.FILES['product_pics'])
                ff.save()
                cloudinary.uploader.upload(f)                 #f.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
        """

def car_detail(request, id):
    single_car = get_object_or_404(Product, pk=id)
    related_pro =  Product.objects.filter(catagory=single_car.catagory).exclude(pk=single_car.id)[:20]
    data = {
        'single_car' : single_car,
        'related_pro': related_pro,
    }
    return render(request, 'ads/ads_detail.html', data)



def ser_detail(request, id):
    single_car = get_object_or_404(Service, pk=id)
    
    related_ser =  Service.objects.filter(catagory=single_car.catagory).exclude(pk=single_car.id)[:20]
    data = {
        'single_car' : single_car,
        'related_ser': related_ser,
        
    }    
    return render(request, 'ads/ser_detail.html', data)


def search(request):
    cars = Product.objects.order_by('-created')

    model_search = Product.objects.values_list('title', flat=True).distinct()
    city_search = Product.objects.values_list('location', flat=True).distinct()
     

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__icontains=model)

    if 'location' in request.GET:
        location = request.GET['location']
        if location:
            cars = cars.filter(city__iexact=location)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    data = {
        'cars' : cars,
        'model_search': model_search,
        'city_search': city_search,
        
    }
    return render(request, 'ads/psearch.html', data)