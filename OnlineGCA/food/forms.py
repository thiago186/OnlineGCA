from django import forms
from .models import Food

class ItemForm(forms.ModelForm):
    class Meta:
        model= Food
        fields= ['item_name', 'item_description', 'item_price', 'item_image']
