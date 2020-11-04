from django import forms
from project_first_app.models import *


class OwnerForm(forms.ModelForm):
    class Meta:

        model = Owner
        fields = 'name', 'surname', 'birth_date'


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            "mark",
            "model",
            "color",
            "state_number",
        ]