from django.contrib import admin
from .models import *


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'first_name',
                    'last_name',
                    'phone_number',
                    'email',
                    'new_post_number'
                    )
    ordering = ('id', )


@admin.register(OrderItems)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id',)
    ordering = ('id', )


