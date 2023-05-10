from django.db import models
from products.models import Products


class OrderItems(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=True, blank=True, default=None)
    size = models.CharField(max_length=10, default='S')
    total_price = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Order Items'

    def __str__(self):
        return str(self.order)


class Order(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField()
    city = models.CharField(max_length=255)
    new_post_number = models.CharField(max_length=255)
    products = models.ManyToManyField(Products, through='OrderItems')

    class Meta:
        verbose_name_plural = 'Orders'

    def __str__(self):
        return str(self.first_name)
