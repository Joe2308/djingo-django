from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    # create an inner class
    class Meta:
        model = Item
        fields = ['name', 'done']
