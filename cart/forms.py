from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    extra = 0
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'city', 'new_post_number']
        widgets = {
            'first_name': forms.TextInput(attrs={'label_tag': 'Your first name'})
        }
