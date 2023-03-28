from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class AllProductsView(ListView):
    model = Products
    template_name = 'products/index.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = {
            'items': Products.objects.all().order_by('-price'),
            'types': ProductType.objects.all(),
        }
        return queryset


class AllProductsFilterView(ListView):
    model = Products
    template_name = 'products/filtered_products.html'
    context_object_name = 'products'

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        queryset = {
            'filtered_items': qs.filter(product_type__product_type=self.kwargs['c_type']).order_by('-price'),
            'types': ProductType.objects.all(),
        }
        return queryset

