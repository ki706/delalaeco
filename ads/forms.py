
from django  import forms
from django.db.models import fields
from django.forms.formsets import BaseFormSet
from django.forms.models import inlineformset_factory 
from django.core.exceptions import ValidationError
from .models import Service, Product
from django.forms import formset_factory 
from django.forms import modelformset_factory
from crispy_forms.layout import Layout, HTML, Column, Row
from crispy_forms.helper import FormHelper


    

class ServiceCreationForm(forms.ModelForm):
     class Meta:
        model = Service
        fields = ('catagory','title','experiance','location','service_pics','service_pics1',
                  'skill','description')   
         
     
class ProductCreationForm(forms.ModelForm):
   class Meta:
      model = Product
      fields = ('catagory','title','price','location','product_pics','product_pics1',
                  'description') 
 