from django.shortcuts import render
from products.models import *


def index_f(request):
    context = {
        'cart': request.session.get('cart', None),
        'types': ProductType.objects.all(),
        'items': Products.objects.all()
    }
    return render(request, 'cart/cart_index.html', context)
