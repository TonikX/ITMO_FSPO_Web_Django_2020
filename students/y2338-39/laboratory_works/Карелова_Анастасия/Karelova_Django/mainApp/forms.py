from .models import Client, Deal, Lawyer, Meeting, Payment
from django.forms import ModelForm, TextInput
from django import forms


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ["name", "phone", "passport"]
        widgets = {
            "name": TextInput(attrs={
                "class": 'form-control',
                "placeholder": 'Richard Nixon'
            }),
            "passport": TextInput(attrs={
                "class": 'form-control',
                "placeholder": '4040400400'

            }),
            "phone": TextInput(attrs={
                "class": 'form-control',
                "placeholder": '895000000000'
            }),
        }


class ClientFormAuto(ModelForm):
    class Meta:
        model = Client
        fields = ["phone", "passport"]
        widgets = {
            "phone": TextInput(attrs={
                "class": 'form-control',
                "placeholder": '895000000000'
            }),
            "passport": TextInput(attrs={
                "class": 'form-control',
                "placeholder": '4040400400',
                "name": 'key_pas'
            }),
        }


class RegistrationForm(ModelForm):
    class Meta:
        model = Deal
        lawyer = forms.ModelChoiceField(queryset=Lawyer.objects.all(), empty_label=None)
        fields = ["date_opened", "date_closed", "lawyer"]
        widgets = {
            "date_opened": TextInput(attrs={
                "class": 'form-control',
                "type": 'date',
                "placeholder": '2020-10-02',
                "name": 'date-entry'
            }),
            "date_closed": TextInput(attrs={
                "class": 'form-control',
                "type": 'date',
                "placeholder": '2020-10-02',
                "name": 'date-entry'
            })
        }


class MeetingForm(ModelForm):
    class Meta:
        model = Meeting
        lawyer = forms.ModelChoiceField(queryset=Lawyer.objects.all(), empty_label=None)
        fields = ["lawyer", "date"]
        widgets = {
            "date": TextInput(attrs={
                "class": 'form-control',
                "type": 'date',
                "placeholder": '2020-10-02',
                "name": 'date-entry'
            })
        }


class PaymentForm(ModelForm):
    class Meta:
        model = Payment
        lawyer = forms.ModelChoiceField(queryset=Lawyer.objects.all(), empty_label=None)
        fields = ["lawyer", "date", "pay_sum"]
        widgets = {
            "date": TextInput(attrs={
                "class": 'form-control',
                "type": 'date',
                "placeholder": '2020-10-02',
                "name": 'date-entry'
            }),
            "pay_sum": TextInput(attrs={
                "class": 'form-control',
                "placeholder": '1000'})
        }