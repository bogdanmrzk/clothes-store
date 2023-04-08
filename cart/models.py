from django.db import models


class OrderItems(models.Model):
    first_name = models.ForeignKey('Order', on_delete=models.PROTECT, default='NAME')
    product_name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Order Items'


class Order(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField()
    city = models.CharField(max_length=255)
    new_post_number = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Orders'
