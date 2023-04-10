from django.db import models


class OrderItems(models.Model):
    first_name = models.ForeignKey('Order', on_delete=models.PROTECT, default='NAME')
    product_name = models.CharField(max_length=255)
    total_price = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Order Items'

    def __str__(self):
        return self.first_name


class Order(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField()
    city = models.CharField(max_length=255)
    new_post_number = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Orders'

    def __str__(self):
        return self.first_name
