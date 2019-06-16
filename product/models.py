from __future__ import unicode_literals

import uuid
import datetime
from decimal import Decimal

from django.db import models
from django.conf import settings
from django_prices.models import PriceField
from django.utils.translation import pgettext_lazy
from django.utils.encoding import python_2_unicode_compatible
from userprofile.models import User


# Create your models here.


""" Universe Model """
@python_2_unicode_compatible
class Product(models.Model):
    name = models.CharField(
        pgettext_lazy('Product field', 'name'), max_length=128)
    is_active = models.BooleanField(
        pgettext_lazy('Product field', 'is deleted'), default=False)
    created_at = models.DateTimeField(auto_now_add=True)    
    updated_at = models.DateTimeField(
        pgettext_lazy('Product field', 'updated at'), auto_now=True, null=True)

    class Meta:
        app_label = 'product'
        verbose_name = pgettext_lazy('Product model', 'product')
        verbose_name_plural = pgettext_lazy('Product model', 'products')

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class VendorProduct(models.Model):
    product = models.ForeignKey(
        Product, related_name='vendor_products',
        verbose_name=pgettext_lazy('Vendor Product field', 'product'), null=True)
    vendor = models.ForeignKey(
        User, related_name='vendor_products',
        verbose_name=pgettext_lazy('Vendor Product field', 'Vendor'), null=True)
    name = models.CharField(
        pgettext_lazy('Vendor Product field', 'name'), max_length=128)    
    active = models.BooleanField(
        pgettext_lazy('Vendor Product field', 'Active'), default=True, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(
        pgettext_lazy('Vendor Product field', 'updated at'), auto_now=True, null=True)

    class Meta:
        app_label = 'product'
        verbose_name = pgettext_lazy('Vendor Product model', 'Vendor product')
        verbose_name_plural = pgettext_lazy('Vendor Product model', 'distributor products')

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class VendorStock(models.Model):
    vendor_product = models.ForeignKey(
        VendorProduct, related_name='vendor_stock',
        verbose_name=pgettext_lazy('Vendor stock field', 'vendor product'),
        null=True, on_delete=models.CASCADE)
    quantity = models.IntegerField(
        pgettext_lazy('Vendor stock field', 'quantity'), default=Decimal(0), blank=True, null=True)
    batch_number = models.CharField(
        pgettext_lazy('Vendor stock field', 'batch_id'), max_length=128, null=True)
    batch_date = models.DateTimeField(
        pgettext_lazy('Vendor stock field', 'batch date'), auto_now=True, null=True)
    mrp = PriceField(
        pgettext_lazy('Vendor stock field', 'MRP'),
        currency=settings.DEFAULT_CURRENCY, max_digits=12, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(
    	pgettext_lazy('Vendor stock field', 'created at'), auto_now=True, null=True)
    updated_at = models.DateTimeField(
    	pgettext_lazy('Vendor stock field', 'updated at'), auto_now=True, null=True)

    class Meta:
        app_label = 'product'

    def __str__(self):
        return '%s' % (self.batch_id)


class Approval(models.Model):
    product = models.ForeignKey(
        Product, related_name='approval_products',
        verbose_name=pgettext_lazy('Product field', 'product'), null=True)
    requested_by = models.ForeignKey(
        User, related_name='requested_user',
        verbose_name=pgettext_lazy('Vendor Product field', 'By user'), null=True)
    approved_by = models.ForeignKey(
        User, related_name='approved_user',
        verbose_name=pgettext_lazy('Vendor Product field', 'User'), null=True)
    is_approved = models.BooleanField(
        pgettext_lazy('Product field', 'is deleted'), default=False)
    created_at = models.DateTimeField(
        pgettext_lazy('Vendor stock field', 'created at'), auto_now=True, null=True)
    updated_at = models.DateTimeField(
        pgettext_lazy('Vendor stock field', 'updated at'), auto_now=True, null=True)    