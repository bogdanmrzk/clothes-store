from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import OrderForm
from products.models import ProductType, Products


class CartIndexView(View):
    def get(self, request):
        context = {
            'cart': request.session.get('cart', {}),
            'item_amount': request.session.get('item_amount'),
            'types': ProductType.objects.all(),
            'items': Products.objects.all(),
            'order_form': OrderForm(),
        }
        return render(request, 'cart/cart_index.html', context)

    def post(self, request):
        item_id = request.POST.get('item_id')
        cart = request.session.get('cart', {})
        if item_id in cart:
            del cart[item_id]
            request.session['cart'] = cart
            request.session['item_amount'] = len(cart)
            return redirect('products:cart:cart_view')
        else:
            return HttpResponse(status=404)
