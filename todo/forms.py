from django import forms
from .models import Item


# inherit django form functionality
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'done']
