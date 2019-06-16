
from django.views.decorators.csrf import csrf_exempt
from userprofile.models import User
from validator import *
from basecontroller import BaseController 
import json
from django.db import transaction
from django.contrib.auth import authenticate
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
                    user = User.objects.get(email=data['email'])
                    return BaseController().respond_with_item(200, user, UserTransformer)
                except Exception as e:
                    print e
                return BaseController().respond_with_error(200, 'oops..something is wrong. We will look into it right away')     
            return BaseController().respond_with_error(200, 'Your Phone/email or password is not correct')
        return BaseController().respond_with_error(200, 'Your Phone/email or password is not correct')
    return BaseController().respond_with_error(404, 'Wow! You found something that we thought did not exist. We will look into it right away')

