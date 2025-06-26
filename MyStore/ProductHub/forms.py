from django import forms
from .models import Product


class ProductForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), label="Select Product",
                                     widget=forms.Select(
            attrs={
                'class': 'text-black bg-white p-1 rounded border border-gray-300 w-[30%] ml-2'
            }
        ))