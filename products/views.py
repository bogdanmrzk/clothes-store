from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .forms import ProductSizeForm
from .models import *


class ProductsBaseView:
    template_name = ''
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['types'] = ProductType.objects.all()
        context['items'] = Products.objects.all()
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
        return context

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Products, item_slug=self.kwargs['item_slug'])
        choice_form = ProductSizeForm(request.POST, product_id=product.id)
        if choice_form.is_valid():
            return HttpResponseRedirect(reverse('clothes_view'))
        else:
            context = self.get_context_data(**kwargs)
            context['size_choice_form'] = choice_form
            return self.render_to_response(context)

