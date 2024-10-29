from django import forms
from .models import Receipt, Product


class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = ['storeName', 'storeAddress', 'totalPrice', 'date']
        labels = {
            'storeName': 'Store Name',
            'storeAddress': 'Store Address',
            'totalPrice': 'Total Price',
            'date': 'Date'
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['receipt', 'name', 'nameEnglish',
                  'nameChinese', 'price', 'discount']
        labels = {
            'receipt': 'Receipt',
            'name': 'Product Name',
            'nameEnglish': 'Name (English)',
            'nameChinese': 'Name (Chinese)',
            'price': 'Price',
            'discount': 'Discount'
        }
        widgets = {
            'receipt': forms.HiddenInput(),
            'nameEnglish': forms.HiddenInput(),
            'nameChinese': forms.HiddenInput(),
        }
