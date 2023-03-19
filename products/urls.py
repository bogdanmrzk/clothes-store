from django.urls import path

from products.views import *

urlpatterns = [
        path('', product_view, name='clothes_view'),
        path('<str:c_type>/', filter_product_view, name='clothes_type_url')
]
