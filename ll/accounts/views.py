from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.utils import timezone
import random
from datetime import timedelta
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import base64
import io
import uuid
from PIL import Image, ImageDraw, ImageFont
from django.core.cache import cache
import requests
from django.forms import ValidationError


from .forms import (
    CustomUserCreationForm, 
    PhoneLoginForm
    )
from .models import PhoneVerification
from .utils import generate_verification_code, send_sms_verification

User = get_user_model()

logger = logging.getLogger(__name__)

def register(request):
    """Register a new user with phone verification."""
    if request.method != 'POST':
        # Display blank registration form.
        form = CustomUserCreationForm()
        context = {'form': form}
        return render(request, 'registration/register.html', context)

    # Process completed form.
    form = CustomUserCreationForm(data=request.POST)
    # Display a blank or invalid form.
    context = {'form': form}
    
    phone_number = request.POST.get('phone_number', '').strip()
    verification_code = request.POST.get('verification_code', '').strip()
    terms_agreement = request.POST.get('terms_agreement') == 'on'

    # Validate form data
    if not phone_number or not verification_code:
        return render(request, 'registration/login.html', {
            'error': 'Phone number and verification code are required',
            'show_code_login': True
        })

    if not terms_agreement:
        return render(request, 'registration/login.html', {
            'error': 'You must agree to the terms and conditions',
            'show_code_login': True
        })

    # Clean phone number
    clean_phone = phone_number.replace('+86', '').replace(' ', '')

    try:
        # Get verification record
        verification = PhoneVerification.objects.get(
            phone_number=phone_number,
            verification_code=verification_code,
            is_verified=False
        )

        # Check if code is expired
        if verification.is_expired():
            form.add_error(None, 'Verification code has expired. Please request a new one.')

            return render(request, 'registration/register.html',context)

        # Mark code as verified
        verification.is_verified = True
        verification.save()

        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            login(request, new_user)
            return redirect('lla1:topics')

        # Handle form validation errors
        if 'phone_number' in form.errors:
            # Get the specific error for phone number
            phone_error = form.errors['phone_number'][0]
            if 'already registered' in phone_error:
                # This is a duplicate phone number error
                form.add_error('phone_number', 'This phone number is already registered.')
        elif 'terms_agreement' in form.errors:
            form.add_error(None, 'You must agree to the Terms of Use and Privacy Policy')

    except PhoneVerification.DoesNotExist:
        form.add_error(None, 'Invalid verification code')

        return render(request, 'registration/register.html', {
            'error': 'Invalid verification code',
            'show_code_login': True
        })
    except Exception as e:
        logger.exception(f"Error in registration: {str(e)}")
        return render(request, 'registration/login.html', {
            'error': 'An error occurred. Please try again.',
            'show_code_login': True
        })

    # Display a blank or invalid form.
    #context = {'form': form}
    return render(request, 'registration/register.html', context)
        

def phone_login(request):
    """Login with phone number and password."""
    if request.method == 'POST':
        form = PhoneLoginForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data.get('phone_number')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=phone_number, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('lla1:topics')
            else:
                messages.error(request, 'Invalid phone number or password.')
    else:
        form = PhoneLoginForm()
    
    return render(request, 'registration/login.html', {'form': form})

@csrf_exempt
def send_verification_code(request):
    """API endpoint to send verification code to phone."""
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        
        if not phone_number:
            return JsonResponse({'success': False, 'message': 'Phone number is required'})
        
        # Generate a random verification code
        code = ''.join(random.choices('0123456789', k=6))
        
        # Store the code in the session or database
        # Here we'll use Django's cache for simplicity
        cache.set(f'phone_verification_{phone_number}', code, timeout=300)  # 5 minutes
        
        # In a real application, you would send an SMS here
        # For now, we'll just return success
        print(f"Verification code for {phone_number}: {code}")  # For testing
        
        return JsonResponse({'success': True, 'message': 'Verification code sent'})
    
    return JsonResponse({'success': False, 'message': 'Invalid request method'})

def sms_login(request):
    """Handle SMS code login submission"""
    if request.method != 'POST':
        return redirect('accounts:login')
 
    phone_number = request.POST.get('phone_number', '').strip()
    verification_code = request.POST.get('verification_code', '').strip()
    terms_agreement = request.POST.get('terms_agreement') == 'on'
    
    # Validate form data
    if not phone_number or not verification_code:
        return render(request, 'registration/login.html', {
            'error': 'Phone number and verification code are required',
            'show_code_login': True
        })
    
    if not terms_agreement:
        return render(request, 'registration/login.html', {
            'error': 'You must agree to the terms and conditions',
            'show_code_login': True
        })
    
    # Clean phone number
    clean_phone = phone_number.replace('+86', '').replace(' ', '')
    
    try:
        # Get verification record
        verification = PhoneVerification.objects.get(
            phone_number=phone_number,
            verification_code=verification_code,
            is_verified=False
        )
        
        # Check if code is expired
        if verification.is_expired():
            return render(request, 'registration/login.html', {
                'error': 'Verification code has expired. Please request a new one.',
                'show_code_login': True
            })
        
        # Mark code as verified
        verification.is_verified = True
        verification.save()
        
        # Get or create user
        user, created = User.objects.get_or_create(
            phone_number=clean_phone,
            defaults={
                'email': f"{clean_phone}@placeholder.com",
                'is_active': True
            }
        )
        
        if created:
            # Set unusable password for new users (they'll only use SMS login)
            user.set_unusable_password()
            user.save()
            logger.info(f"New user created with phone: {phone_number}")
        
        # Login the user
        login(request, user)
        
        # Redirect to homepage or dashboard
        return redirect('lla1:topics')  # Change to your target URL
        
    except PhoneVerification.DoesNotExist:
        return render(request, 'registration/login.html', {
            'error': 'Invalid verification code',
            'show_code_login': True
        })
    except Exception as e:
        logger.exception(f"Error in SMS login: {str(e)}")
        return render(request, 'registration/login.html', {
            'error': 'An error occurred. Please try again.',
            'show_code_login': True
        })

def register_bak(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            login(request, new_user)
            return redirect('lla1:index')
        
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)
        

def login_view(request):
    """Main login view"""
    if request.method == 'POST':
        # Your existing login logic here
        pass  # Replace with actual code
    
    # Make sure this return statement is properly indented
    return render(request, 'registration/login.html', {'show_code_login': True})

@csrf_exempt
def generate_visual_captcha(request):
    """Generate a visual CAPTCHA with 3D shapes"""
    # Define possible shapes and colors
    shapes = ['cube', 'sphere', 'pyramid', 'cone', 'cylinder']
    colors = ['red', 'blue', 'green', 'yellow', 'orange']
    
    # Choose a random set of shapes and colors
    captcha_objects = []
    used_combinations = set()
    
    # Generate 5-7 random shape/color combinations
    num_objects = random.randint(5, 7)
    
    for _ in range(num_objects):
        shape = random.choice(shapes)
        color = random.choice(colors)
        
        # Ensure we don't have exact duplicates
        while (shape, color) in used_combinations:
            shape = random.choice(shapes)
            color = random.choice(colors)
            
        used_combinations.add((shape, color))
        captcha_objects.append({'shape': shape, 'color': color})
    
    # Randomly select a shape and color for the prompt
    prompt_shape = random.choice(shapes)
    prompt_color = random.choice(colors)
    
    # Ensure at least one object matches the prompt
    if not any(obj['shape'] == prompt_shape and obj['color'] == prompt_color for obj in captcha_objects):
        # Replace a random object with the prompt shape and color
        replace_idx = random.randint(0, len(captcha_objects) - 1)
        captcha_objects[replace_idx] = {'shape': prompt_shape, 'color': prompt_color}
    
    # Find all objects that match the prompt
    matching_objects = [i for i, obj in enumerate(captcha_objects) 
                        if obj['shape'] == prompt_shape and obj['color'] == prompt_color]
    correct_index = random.choice(matching_objects) if matching_objects else -1
    
    # Generate a challenge prompt
    prompt = f"Click on the {prompt_color} {prompt_shape} in the picture"
    
    # Generate a token and store the correct answer
    token = str(uuid.uuid4())
    cache.set(f"visual_captcha_{token}", correct_index, timeout=300)  # 5 minutes expiry
    
    return JsonResponse({
        'success': True,
        'objects': captcha_objects,
        'prompt': prompt,
        'token': token
    })

@csrf_exempt
def verify_visual_captcha(request):
    """Verify a visual CAPTCHA where user clicks on an object"""
    if request.method != 'POST':
        return JsonResponse({'success': False, 'message': 'Method not allowed'}, status=405)
    
    phone_number = request.POST.get('phone_number', '').strip()
    selected_index = request.POST.get('selected_index')
    token = request.POST.get('token', '')
    
    if not phone_number or selected_index is None or not token:
        return JsonResponse({'success': False, 'message': 'Missing required fields'}, status=400)
    
    try:
        selected_index = int(selected_index)
    except ValueError:
        return JsonResponse({'success': False, 'message': 'Invalid selection'})
    
    # Verify CAPTCHA
    stored_index = cache.get(f"visual_captcha_{token}")
    if stored_index is None:
        return JsonResponse({'success': False, 'message': 'CAPTCHA expired or invalid'})
    
    if selected_index != stored_index:
        return JsonResponse({'success': False, 'message': 'Incorrect selection, please try again'})
    
    # Delete the used CAPTCHA
    cache.delete(f"visual_captcha_{token}")
    
    # Generate and send verification code
    code = generate_verification_code()
    
    # Store or update verification code in database
    PhoneVerification.objects.update_or_create(
        phone_number=phone_number,
        defaults={
            'verification_code': code,
            'created_at': timezone.now(),
            'is_verified': False
        }
    )
    
    # Send SMS via Alibaba Cloud
    result = send_sms_verification(phone_number, code)
    
    if result['success']:
        return JsonResponse({
            'success': True, 
            'message': 'Verification code sent successfully'
        })
    else:
        logger.error(f"Failed to send SMS: {result['message']} to {phone_number}")
        return JsonResponse({
            'success': False, 
            'message': 'Failed to send verification code. Please try again later.'
        })

def wechat_callback(request):
    code = request.GET.get('code')
    if not code:
        return redirect('accounts:login')

    # Exchange code for access token
    app_id = 'YOUR_WECHAT_APP_ID'
    app_secret = 'YOUR_WECHAT_APP_SECRET'
    token_url = f'https://api.weixin.qq.com/sns/oauth2/access_token?appid={app_id}&secret={app_secret}&code={code}&grant_type=authorization_code'
    response = requests.get(token_url)
    data = response.json()

    if 'access_token' in data:
        access_token = data['access_token']
        openid = data['openid']

        # Fetch user info
        user_info_url = f'https://api.weixin.qq.com/sns/userinfo?access_token={access_token}&openid={openid}'
        user_info_response = requests.get(user_info_url)
        user_info = user_info_response.json()

        # Handle user login or registration with user_info
        # ...

    return redirect('accounts:login')

# Create your views here.
