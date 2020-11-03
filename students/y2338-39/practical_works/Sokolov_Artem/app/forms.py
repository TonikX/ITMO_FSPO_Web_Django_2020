from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'modal-form-field-input',
            'placeholder': 'Username'
        })

        self.fields['password1'].widget.attrs.update({
            'class': 'modal-form-field-input',
            'placeholder': 'Password'
        })

        self.fields['password2'].widget.attrs.update({
            'class': 'modal-form-field-input',
            'placeholder': 'Password confirmation'
        })