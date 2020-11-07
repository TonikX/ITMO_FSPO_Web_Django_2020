from django import forms
from .models import *


class AddItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = [
            "title",
            "sort",
            "variety",
            "prise",
            "organizations"
        ]


class AddResForm(forms.ModelForm):
    class Meta:
        model = Results
        fields = [
            "item",
            "organizations",
            "fair",
            "sell_variety",
            "sell_prise",
            "buyer"
        ]