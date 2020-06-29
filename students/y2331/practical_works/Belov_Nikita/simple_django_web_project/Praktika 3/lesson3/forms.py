from django import forms
from .models import Owner, Car


class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner

        fields = ["usr", "first_name", "last_name", "birthday"]


