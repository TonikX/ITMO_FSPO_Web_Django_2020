from django import forms
from .models import Deus, Machina


class DeusForm(forms.ModelForm):
    class Meta:
        model = Deus
        fields = '__all__'

