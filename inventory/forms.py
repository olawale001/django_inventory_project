from django import forms
from .models import Item, Ingredient, Order

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'quantity', 'price', 'expiration_date']



class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name', 'quantity', 'unit']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'items']