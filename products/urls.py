from django.urls import path, include

from products.views import *

app_name = 'products'

urlpatterns = [
        path('', AllProductsView.as_view(), name='clothes_view'),
        path('cart/', include('cart.urls')),
        path('<str:c_type>/', AllProductsFilterView.as_view(), name='clothes_type_url'),
        path('<str:c_type>/<slug:item_slug>/', ProductDetailView.as_view(), name='detail_clothes_view'),
]
