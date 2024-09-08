from django import forms
from invApp.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'id': 'Product ID',
            'name': 'Name',
            'sku': 'Sku',
            'price': 'Price',
            'quantity': 'Quantity',
            'supplier': 'Supplier',
        }
        widgets = {
            'id': forms.NumberInput(
                attrs={'placeholder': 'e.g 1', 'class': 'form-control'}
            ),
            'name': forms.TextInput(
                attrs={'placeholder': 'e.g shirt', 'class': 'form-control'}
            ),
            'sku': forms.TextInput(
                attrs={'placeholder': 'e.g A5212', 'class': 'form-control'}
            ),
            'price': forms.NumberInput(
                attrs={'placeholder': 'e.g 9.99', 'class': 'form-control'}
            ),
            'quantity': forms.NumberInput(
                attrs={'placeholder': 'e.g 10', 'class': 'form-control'}
            ),
            'supplier': forms.TextInput(
                attrs={'placeholder': 'e.g Fedex', 'class': 'form-control'}
            )
        }
