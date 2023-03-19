from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class AllProductsView(ListView):
    template_name = 'products/index.html'


def product_view(request):
    all_products = Products.objects.all().order_by('-price')
    all_types = ProductType.objects.all()
    context = {
        'products': all_products,
        'types': all_types,
    }
    return render(request, template_name='products/index.html', context=context)


def filter_product_view(request, c_type):
    filtered_products = Products.objects.filter(product_type__product_type=c_type).order_by('-price')
    all_types = ProductType.objects.all()
    context = {
        'filtered_products': filtered_products,
        'types': all_types,
    }
    return render(request, template_name='products/filtered_products.html', context=context)


def type_view(request):
    all_types = ProductType.objects.all()
    context = {
        'types': all_types,
    }
    return render(request, template_name='include/dropdown_menu.html', context=context)
