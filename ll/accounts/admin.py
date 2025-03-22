from django.contrib import admin
#from django.contrib.auth import get_user_model
from .models import CustomUser
from .models import PhoneVerification

#User = get_user_model()

# Register your models here.

#admin.site.register(CustomUser)
#admin.site.register(PhoneVerification)

# Register the CustomUser model
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'email', 'is_active', 'date_joined')
    search_fields = ('phone_number', 'email')
    list_filter = ('is_active', 'is_staff', 'date_joined')
    ordering = ('-date_joined',)

# Register the PhoneVerification model
@admin.register(PhoneVerification)
class PhoneVerificationAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'verification_code', 'created_at', 'is_verified')
    search_fields = ('phone_number',)
    list_filter = ('is_verified', 'created_at')
    ordering = ('-created_at',) 