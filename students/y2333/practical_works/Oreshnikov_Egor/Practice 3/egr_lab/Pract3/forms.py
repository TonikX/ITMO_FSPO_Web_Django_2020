from .models import User, People
from django import forms

class UserForm(forms.ModelForm):
     class Meta:
         model = User
         fields = [
             "people",
             "first_name",
             "second_name"
         ]


