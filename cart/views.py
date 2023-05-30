from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.contrib.sessions.models import Session
from .forms import OrderForm
from products.models import ProductType, Products, ProductSize
from .models import Order, OrderItems

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
        return render(request, 'products/base.html', context)

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
                order = Order.objects.create(
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    phone_number=form.cleaned_data['phone_number'],
                    email=form.cleaned_data['email'],
                    city=form.cleaned_data['city'],
                    new_post_number=form.cleaned_data['new_post_number']
                )
                for item_id in request.session['cart']:
                    product = Products.objects.get(pk=item_id)
                    size = request.session['cart'][item_id]['size']
                    product_size = get_object_or_404(ProductSize, product=product, size=size)
                    if product_size.quantity < 2:
                        product_size.delete()
                    else:
                        product_size.quantity -= 1
                        product_size.save()
                    OrderItems.objects.create(
                        order=order,
                        product=product,
                        total_price=request.session['cart'][item_id]['price'],
                        size=request.session['cart'][item_id]['size']
                    )
                else:
                    del request.session['cart']
                    del request.session['item_amount']
                return redirect('products:clothes_view')
            else:
                return HttpResponse(status=400)
