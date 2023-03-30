from django import forms
from django.forms import ModelForm
from .models import *

# class SelectSize(forms.Form):
#     size = forms.CharField(label='Select size', widget=forms.Select(choices=ProductSize.size_choice))


class SelectSize(ModelForm):
    class Meta:
        model = ProductSize
        fields = ['size', ]
