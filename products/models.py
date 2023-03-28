from django.db import models
from django.urls import reverse


class ProductType(models.Model):
    product_type = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Product Types'
        verbose_name = 'Product Type'

    def __str__(self):
        return self.product_type


class Products(models.Model):
    name = models.CharField(max_length=250)
    item_slug = models.SlugField(max_length=255, db_index=True, unique=True)

    class Size(models.TextChoices):
        S = 'Small'
        M = 'Medium'
        L = 'Large'

    image = models.ImageField(upload_to='photos')
    size = models.CharField(max_length=25, choices=Size.choices, default=Size.S)
    description = models.TextField()
    price = models.IntegerField()
    product_type = models.ForeignKey('ProductType', on_delete=models.PROTECT, blank=False)

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse('clothes_type_url', kwargs={'c_type': self.product_type})

    def __str__(self):
        return self.name
