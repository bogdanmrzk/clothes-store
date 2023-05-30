from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from .forms import ProductSizeForm
from .models import *
from online_store import settings


class ProductsBaseView:
    template_name = ''
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['types'] = ProductType.objects.all()
        context['items'] = Products.objects.all()
        context['photos'] = Photo.objects.all()
        context['cart'] = self.request.session.get('cart', {})
        cart = self.request.session.get('cart', {})
        context['item_amount'] = len(cart)
        return context


class AllProductsView(ProductsBaseView, ListView):
    model = Products
    template_name = 'products/index.html'


class AllProductsFilterView(ProductsBaseView, ListView):
    model = Products
    template_name = 'products/filtered_products.html'

    def get_queryset(self, **kwargs):
        qs = super().get_queryset()
        queryset = {
            'filtered_items': qs.filter(product_type__product_type=self.kwargs['c_type']).order_by('-price'),
        }
        return queryset


class ProductDetailView(ProductsBaseView, DetailView):
    model = Products
    template_name = 'products/product_detail.html'
    slug_url_kwarg = 'item_slug'
    slug_field = 'item_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = get_object_or_404(Products, item_slug=self.kwargs['item_slug'])
        choice_form = ProductSizeForm(product_id=product.id)
        context['size_choice_form'] = choice_form
        context['product'] = product
        return context

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Products, item_slug=self.kwargs['item_slug'])
        choice_form = ProductSizeForm(request.POST, product_id=product.id)
        if choice_form.is_valid():
            request.session.set_expiry(settings.SESSION_COOKIE_AGE)
            size = choice_form.cleaned_data['size']
            cart = request.session.get('cart', {})
            cart[str(product.id)] = {
                'name': product.name,
                'price': product.price,
                'image': product.photos.first().image.url if product.photos.exists() else '',
                'size': str(size),
            }
            request.session['cart'] = cart
            request.session['item_amount'] = len(cart)
            return redirect('products:clothes_view')
        else:
            context = self.get_context_data(**kwargs)
            context['size_choice_form'] = choice_form
            return self.render_to_response(context)
