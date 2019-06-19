from __future__ import unicode_literals

import uuid
import datetime

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import pgettext_lazy
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.contrib.auth.models import UserManager

# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        '''Creates a User with the given email and password'''
        user = self.model(email=email, **extra_fields)
        if password:
            user.set_password(password)
        user.save()
        return user
        
    def create_superuser(self, email, password=None, **extra_fields):
        return self.create_user(email, password, is_superuser=True, **extra_fields)

""" Role Model """
@python_2_unicode_compatible
class Roles(models.Model):
    name = models.CharField(
        pgettext_lazy('Role Field', 'Role name'), max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null = True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

""" User Model """
class User(PermissionsMixin, AbstractBaseUser):
    is_vendor = models.BooleanField(default=False)
    email = models.CharField(pgettext_lazy('User field', 'email'), null=True, max_length=50, unique=True) 
    roles = models.ManyToManyField(Roles, related_name="roles", blank=True)
    date_joined = models.DateTimeField(
        pgettext_lazy('User field', 'date joined'),
        default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    class Meta:
        verbose_name = pgettext_lazy('User model', 'user')
        verbose_name_plural = pgettext_lazy('User model', 'users')













    