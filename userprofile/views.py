import json, jwt

from django.db import transaction
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.settings import APISettings
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes


from userprofile.models import User
from validator import *
from basecontroller import BaseController 
from transformer import UserTransformer


"""Sign Up User Retailer
@param request obj
@return success message
"""
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if validate_signup(data):
            try:
                with transaction.atomic():
                    extra_fields = {}
                    email = data['email']
                    extra_fields['is_vendor'] = data['isVendor']
                    is_exists = User.objects.filter(email=email)
                    if is_exists:
                        return BaseController().respond_with_error(200, 'This email is registered already')
                    user = User.objects.create(email=email,
                                                 **extra_fields )
                    user.set_password(data['password'])
                    user.save()
                    return BaseController().respond_with_success(200, 'User created successfully')
                return BaseController().respond_with_error(200, 'User not registered. We will look into it')
            except Exception as e:
                print e
                return BaseController().respond_with_error(200, 'This phone number is already registered')        
        return BaseController().respond_with_error(200, 'Fields are missing, please update')
    return BaseController().respond_with_error(404, 'Wow! You found something that we thought did not exist. We will look into it right away.')



@csrf_exempt
# @api_view(['POST'])
def login(request):
    if request.method == 'POST':
        credentials = {}
        data = json.loads(request.body)
        if validate_login(data):
            password = data['password']
            credentials['email'] = data['email']
            credentials['password'] = data['password']
            if authenticate(username = data['email'], password=data['password']) is not None:
                try:
                    # payload = APISettings.jwt_payload_handler(credentials)
                    user = User.objects.get(email=data['email'])
                    encoded_token = jwt.encode({'email': data['email'], 'userId': user.id }, 'SECRET', algorithm='HS256')
                    encoded_token = "Bearer {0}".format(encoded_token)
                    # token = jwt.encode(payload, settings.SECRET_KEY)
                    return BaseController().respond_with_item(200, user, UserTransformer, encoded_token)
                except Exception as e:
                    print e
                return BaseController().respond_with_error(200, 'oops..something is wrong. We will look into it right away')     
            return BaseController().respond_with_error(200, 'Your Phone/email or password is not correct')
        return BaseController().respond_with_error(200, 'Your Phone/email or password is not correct')
    return BaseController().respond_with_error(404, 'Wow! You found something that we thought did not exist. We will look into it right away')

