from django.contrib import admin
from .models import *


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("name", 'size', 'price',)
    prepopulated_fields = {"item_slug": ("name",)}


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('product_type',)
