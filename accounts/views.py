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
    clean_phone = phone_number.replace('+', '').replace(' ', '')
    
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
        
        # Get or create user using phone_number field instead of username
        user, created = User.objects.get_or_create(
            phone_number=clean_phone,
            defaults={
                'email': f"{clean_phone}@placeholder.com",
                'is_active': True
            }
        )
        
        # Login the user
        login(request, user)
        
        # Redirect to homepage or dashboard
        return redirect('home')  # Change to your target URL
        
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