from django.urls import path

from cart.views import *

app_name = 'cart'

urlpatterns = [
        path('', index_f, name='cart_view'),
]
