from django import forms
from .models import Item

# use django to create form and rendder as template var
# inherit django form functionality
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'done']
