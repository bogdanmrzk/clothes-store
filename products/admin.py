from django.contrib import admin
from .models import *


@admin.register(ProductSize)
class SizesAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity', 'size',)
    list_editable = ('quantity', 'size')
    list_display_links = ('id', 'product',)
    ordering = ('product',)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price',)
    prepopulated_fields = {'item_slug': ('name',)}


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('product_type',)
