from django.urls import path

from cart.views import *

app_name = 'cart'

urlpatterns = [
        path('', CartIndexView.as_view(), name='cart_view'),
]
