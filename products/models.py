from django.db import models
from django.urls import reverse
from django.db.models import Case, When


class ProductSize(models.Model):
    product = models.ForeignKey('Products', on_delete=models.CASCADE)

    SIZE_CHOICES_CLOTHES = [
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
    ]

    quantity = models.PositiveIntegerField(default=0)
    size = models.CharField(max_length=25, choices=SIZE_CHOICES_CLOTHES, default='S')

    class Meta:
        ordering = [
            Case(
                When(size='S', then=0),
                When(size='M', then=1),
                When(size='L', then=2),
                default=5,
                output_field=models.IntegerField(),
                )
        ]

    def __str__(self):
        return self.size


class ProductType(models.Model):
    product_type = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Product Types'
        verbose_name = 'Product type'

    def __str__(self):
        return self.product_type


class Products(models.Model):
    name = models.CharField(max_length=255)
    item_slug = models.SlugField(max_length=255)
    image = models.ImageField(upload_to='photos')
    description = models.TextField()
    price = models.IntegerField()
    product_type = models.ForeignKey('ProductType', on_delete=models.PROTECT, blank=False, related_name="product_types")

    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('name',)

    def get_sizes(self):
        return ProductSize.objects.filter(product=self)

    def get_absolute_url(self):
        return reverse("detail_clothes_view", kwargs={"slug": self.item_slug})

    def __str__(self):
        return self.name

