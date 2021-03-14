from django import forms
from .models import *


class DeliverForm(forms.ModelForm):
    class Meta:
        model = Deliver
        fields = [
            "id_deliver",
            "date_of_acceptance",
            "date_of_execution",
        ]


class FlowerForm(forms.ModelForm):
    class Meta:
        model = Flower
        fields = [
            'flower_id',
            'name',
            'sort',
            'cost',
        ]


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = [
            'id_contract',
            'id_deliver',
        ]


class CompositionForm(forms.ModelForm):
    class Meta:
        model = Composition
        fields = [
            'composition_id',
            'title',
            'flower_id',
            'id_contract',
        ]
