from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
import re
import random
from datetime import datetime, timedelta
from django.utils import timezone
from django.core.validators import RegexValidator
from .models import CustomUser

User = get_user_model()

class PhoneNumberField(forms.CharField):
    """Custom field for phone number validation."""
    def validate(self, value):
        super().validate(value)
        # Simple validation for phone numbers (can be enhanced based on your requirements)
        if not re.match(r'^\+?1?\d{10,15}$', value):
            raise ValidationError('Enter a valid phone number.')
        return value

class CustomUserCreationForm(UserCreationForm):
    """Form for user registration with phone number."""
    phone_number = forms.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            ),
        ],
        required=True
    )
    
    verification_code = forms.CharField(max_length=6, required=True)
    terms_agreement = forms.BooleanField(required=True)
    
    class Meta:
        model = CustomUser
        fields = ('phone_number', 'password1', 'password2')
    
    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if CustomUser.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError('This phone number is already registered.')
        return phone_number

class PhoneLoginForm(forms.Form):
    """Form for logging in with phone number and password."""
    phone_number = PhoneNumberField(label="Phone Number")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

