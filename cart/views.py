from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.contrib.sessions.models import Session
from .forms import OrderForm
from products.models import ProductType, Products, ProductSize

main_session = Session.objects.all()


class CartIndexView(View):
    def get(self, request):
        context = {
            'cart': request.session.get('cart', {}),
            'item_amount': request.session.get('item_amount'),
            'total': 0,
            'types': ProductType.objects.all(),
            'items': Products.objects.all(),
            'order_form': OrderForm(),
        }
        for price in context['cart'].values():
            context['total'] += price['price']
        return render(request, 'cart/cart_index.html', context)

    def post(self, request):
        if 'item_id' in request.POST:
            item_id = request.POST.get('item_id')
            cart = request.session.get('cart', {})
            if item_id in cart:
                del cart[item_id]
                request.session['cart'] = cart
                request.session['item_amount'] = len(cart)
                return redirect('products:cart:cart_view')
            else:
                return HttpResponse(status=404)
        elif 'db_form' in request.POST:
            form = OrderForm(request.POST)
            if form.is_valid():
                form.save()
                for item_id in request.session['cart']:
                    product = Products.objects.get(pk=item_id)
                    size = request.session['cart'][item_id]['size']
                    product_size = get_object_or_404(ProductSize, product=product, size=size)
                    product_size.quantity -= 1
                    product_size.save()
                del request.session['cart']
                return redirect('products:clothes_view')
