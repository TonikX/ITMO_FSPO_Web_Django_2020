from django import forms
from .models import User, Avtom


class Useradd(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "passportnum",
        ]