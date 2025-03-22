from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
import datetime

# Create your models here.
class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with phone number as the unique identifier."""

    def create_user(self, phone_number, password=None, **extra_fields):
        """Create and save a User with the given phone number and password."""
        if not phone_number:
            raise ValueError(_('The Phone Number must be set'))
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        """Create and save a SuperUser with the given phone number and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(phone_number, password, **extra_fields)

class CustomUser(AbstractUser):
    """Custom User model with phone number as the unique identifier."""
    username = None
    phone_number = models.CharField(_('phone number'), max_length=15, unique=True)
    sms_code = models.CharField(max_length=6, blank=True, null=True)
    sms_code_expiry = models.DateTimeField(blank=True, null=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.phone_number

class PhoneVerification(models.Model):
    phone_number = models.CharField(max_length=20, unique=True)
    verification_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    
    def is_expired(self):
        """Check if verification code is expired (10 minutes)"""
        expiration_time = self.created_at + datetime.timedelta(minutes=10)
        return timezone.now() > expiration_time
    
    def __str__(self):
        return f"{self.phone_number} - {self.verification_code}"
