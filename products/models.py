from django.db import models
from django.urls import reverse


class ProductSize(models.Model):
    name = models.ForeignKey('Products', on_delete=models.PROTECT, blank=False, default='product')

    class Size(models.TextChoices):
        S = 'Small'
        M = 'Medium'
        L = 'Large'

    quantity = models.IntegerField(default=0)
    size = models.CharField(max_length=25, choices=Size.choices, default=Size.S)


class ProductType(models.Model):
    product_type = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Product Types'
        verbose_name = 'Product Type'

    def __str__(self):
        return self.product_type


class Products(models.Model):
    name = models.CharField(max_length=255)
    item_slug = models.SlugField(max_length=255, db_index=True, unique=True)
    image = models.ImageField(upload_to='photos')
    description = models.TextField()
    price = models.IntegerField()
    product_type = models.ForeignKey('ProductType', on_delete=models.PROTECT, blank=False, related_name="product_types")

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse("detail_clothes_view", kwargs={"slug": self.item_slug})

    def __str__(self):
        return self.name
