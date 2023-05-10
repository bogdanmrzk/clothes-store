from django.contrib import admin
from .models import Order, OrderItems


class OrderItemsInline(admin.TabularInline):
    model = OrderItems
    extra = 0



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemsInline]
    list_display = ['id',
                    'first_name',
                    'last_name',
                    'phone_number',
                    'email',
                    'city',
                    'new_post_number',
                    'order_items',
                    ]

    def order_items(self, obj):
        items = OrderItems.objects.all()
        return ', '.join(str(item.product) for item in items)

    order_items.short_description = 'Order Items'
