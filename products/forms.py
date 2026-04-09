from django import forms
from .models import Product

class ProductForm(forms.Form):
    name = forms.CharField(max_length=200, label="Name")
    description = forms.CharField(label="Description", widget=forms.Textarea)
    price = forms.DecimalField(max_digits=10, decimal_places=2, label="Price")
    available = forms.BooleanField(initial=True, label="Available", required=False)
    photo = forms.ImageField(label="Picture", required=False)
    stock = forms.IntegerField(initial=0, label="Stock") 

    def save(self):
        Product.objects.create(
            name=self.cleaned_data['name'],
            description=self.cleaned_data['description'],
            price=self.cleaned_data['price'],
            available=self.cleaned_data['available'],
            photo=self.cleaned_data['photo'],
            stock=self.cleaned_data['stock'],

        )