from django import forms
from .models import ProductSize


class ProductSizeForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        product_id = kwargs.pop('product_id', None)
        super(ProductSizeForm, self).__init__(*args, **kwargs)
        self.fields['size'].queryset = ProductSize.objects.filter(product_id=product_id)

    size = forms.ModelChoiceField(
        queryset=ProductSize.objects.filter(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label='Choose an option'
    )

    class Meta:
        model = ProductSize
        fields = ('size',)

