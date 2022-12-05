from django.db import models
from django.contrib.auth.models import AbstractUser

from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class CustomUser(AbstractUser):
    phone_number = PhoneNumberField(unique=True, verbose_name=_('PhoneNumber'))
    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
