import json
import random
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from django.conf import settings

# Get these values from your Alibaba Cloud account
ACCESS_KEY_ID = settings.ALIYUN_ACCESS_KEY_ID
ACCESS_KEY_SECRET = settings.ALIYUN_ACCESS_KEY_SECRET
SIGN_NAME = settings.ALIYUN_SMS_SIGN_NAME
TEMPLATE_CODE = settings.ALIYUN_SMS_TEMPLATE_CODE

def generate_verification_code():
    """Generate a random 6-digit verification code"""
    return str(random.randint(100000, 999999))

def send_sms_verification(phone_number, verification_code):
    """
    Send SMS verification code using Alibaba Cloud SMS
    
    Args:
        phone_number (str): The phone number to send the code to (with country code)
        verification_code (str): The 6-digit verification code
        
    Returns:
        dict: Response from Alibaba Cloud SMS API
    """
    # Remove '+' and spaces from phone number if present
    phone_number = phone_number.replace('+', '').replace(' ', '')
    
    # Initialize ACS client
    client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, 'cn-hangzhou')
    
    # Create request
    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')
    
    # Set request parameters
    request.add_query_param('PhoneNumbers', phone_number)
    request.add_query_param('SignName', SIGN_NAME)
    request.add_query_param('TemplateCode', TEMPLATE_CODE)
    
    # Set template parameters - customize based on your template
    template_param = {"code": verification_code}
    request.add_query_param('TemplateParam', json.dumps(template_param))
    
    # Send request
    try:
        response = client.do_action_with_exception(request)
        response_json = json.loads(response.decode('utf-8'))
        return {
            'success': response_json.get('Code') == 'OK',
            'message': response_json.get('Message'),
            'detail': response_json
        }
    except Exception as e:
        return {
            'success': False,
            'message': str(e),
            'detail': None
        } 