from django import forms
from .models import ProductSize, Products


class ProductSizeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductSizeForm, self).__init__(*args, **kwargs)
        self.fields['size'].queryset = ProductSize.objects.filter(product_id=self.instance.product.pk)

    size = forms.ModelChoiceField(
        queryset=ProductSize.objects.filter(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = ProductSize
        fields = ('size', )
