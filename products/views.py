from django.views.generic import ListView, DetailView
from .forms import ProductSizeForm
from .models import *


class AllProductsView(ListView):
    model = Products
    template_name = 'products/index.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super(AllProductsView, self).get_context_data(**kwargs)
        context['types'] = ProductType.objects.all()
        context['items'] = Products.objects.all()
        return context


class AllProductsFilterView(ListView):
    model = Products
    template_name = 'products/filtered_products.html'
    context_object_name = 'products'

    def get_queryset(self, **kwargs):
        qs = super().get_queryset()
        queryset = {
            'filtered_items': qs.filter(product_type__product_type=self.kwargs['c_type']).order_by('-price'),
        }
        return queryset

    def get_context_data(self, **kwargs):
        context = super(AllProductsFilterView, self).get_context_data(**kwargs)
        context['types'] = ProductType.objects.all()
        context['items'] = Products.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Products
    template_name = 'products/product_detail.html'
    context_object_name = 'products'
    slug_url_kwarg = 'item_slug'
    slug_field = 'item_slug'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['types'] = ProductType.objects.all()
        context['items'] = Products.objects.all()
        context['size_choice_form'] = ProductSizeForm
        return context
