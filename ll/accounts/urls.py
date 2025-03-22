"""define url patterns for accounts app"""

from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

app_name = 'accounts'

urlpatterns = [
    # Login views
    path('login/', views.phone_login, name='login'),
    path('sms-login/', views.sms_login, name='sms_login'),
        
    # Registration view
    path('register/', views.register, name='register'), 
       
    # Logout view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('send-verification-code/', views.send_verification_code, name='send_verification_code'),
    path('generate-visual-captcha/', views.generate_visual_captcha, name='generate_visual_captcha'),
    path('verify-visual-captcha/', views.verify_visual_captcha, name='verify_visual_captcha'),
]