from django.contrib import admin
from django.urls import path

from products.views import *

urlpatterns = [
        path('', AllProductsView.as_view(), name='clothes_view'),
        path('<str:c_type>/', AllProductsFilterView.as_view(), name='clothes_type_url')
]
