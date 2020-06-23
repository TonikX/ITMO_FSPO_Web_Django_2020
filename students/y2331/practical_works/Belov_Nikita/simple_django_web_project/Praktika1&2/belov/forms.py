from django import forms
from .models import Car, User, CarUser

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["carMake", "carModel", "prodYear"]


