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

    objects = UserManager()

    USERNAME_FIELD = 'email'
    class Meta:
        verbose_name = pgettext_lazy('User model', 'user')
        verbose_name_plural = pgettext_lazy('User model', 'users')













    