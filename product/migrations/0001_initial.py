# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-06-15 08:58
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion
import django_prices.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Approval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True, null=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='updated at')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('is_active', models.BooleanField(default=False, verbose_name='is deleted')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='updated at')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
        migrations.CreateModel(
            name='VendorProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='name')),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='updated at')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vendor_products', to='product.Product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'Vendor product',
                'verbose_name_plural': 'distributor products',
            },
        ),
        migrations.CreateModel(
            name='VendorStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=Decimal('0'), null=True, verbose_name='quantity')),
                ('batch_number', models.CharField(max_length=128, null=True, verbose_name='batch_id')),
                ('batch_date', models.DateTimeField(auto_now=True, null=True, verbose_name='batch date')),
                ('mrp', django_prices.models.PriceField(currency=b'INR', decimal_places=2, default=0.0, max_digits=12, verbose_name='MRP')),
                ('created_at', models.DateTimeField(auto_now=True, null=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, null=True, verbose_name='updated at')),
                ('vendor_product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vendor_stock', to='product.VendorProduct', verbose_name='vendor product')),
            ],
        ),
    ]