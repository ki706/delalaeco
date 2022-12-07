 
from django import forms
from django.forms import fields
from .models import CustomUser
from allauth.account.forms import SignupForm
from django.core.validators import MaxValueValidator,MinValueValidator
from phonenumber_field.formfields import PhoneNumberField
from django.db import IntegrityError
from .models import CustomUser
from django.shortcuts import get_object_or_404, reverse, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
class MyCustomSignupForm(SignupForm):
        phone_number = PhoneNumberField(region="ET", label = "Phone")
        #tg_link = forms.CharField(max_length=15)
        #email = forms.EmailField(label="E-mhhhhail")
        #password1 = forms.PasswordField(label="")
        phone_number.error_messages['invalid'] = 'Use correct format eg 0920302030'
        
        def clean_phone_number(self):
            #super(MyCustomSignupForm, self).clean()
            phone_number = self.cleaned_data['phone_number']
            phone_number = self.cleaned_data.get("phone_number")
            msg = 'A user is already registered with this phone'
            if CustomUser.objects.filter(phone_number=phone_number).exists():
                #self._errors['phone_number'] = self.error_class([msg])
               
                raise forms.ValidationError(msg)
            else:
                return phone_number         
        
        def save(self, request):
          
            user = super(MyCustomSignupForm, self).save(request)
            user.phone_number = self.cleaned_data['phone_number']
            #user.p_number = self.cleaned_data['p_number']
            #user.tg_link = self.cleaned_data['tg_link']
           
            user.save()
            return user
          