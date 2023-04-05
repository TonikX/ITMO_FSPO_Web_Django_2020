from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class TrainForm(forms.ModelForm):
    class Meta:
        model = Train
        fields = ('reg_number', 'departure', 'destination', 'date_time_departure', 'date_time_destination')
        widgets = {
            'reg_number': forms.TextInput(attrs={'class': 'form-control'}),
            'departure': forms.TextInput(attrs={'class': 'form-control'}),
            'destination': forms.TextInput(attrs={'class': 'form-control'}),
            'date_time_departure': forms.TextInput(attrs={'class': 'form-control'}),
            'date_time_destination': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CarriageForm(forms.ModelForm):
    class Meta:
        model = Carriage
        fields = ('reg_number_train', 'number', 'type', 'number_of_seats', 'price')
        widgets = {
            'reg_number_train': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'number_of_seats': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SeatForm(forms.ModelForm):
    class Meta:
        model = Seat
        fields = ('id_carriage', 'number', 'status')
        widgets = {
            'id_carriage': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
        }


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('name', 'number_passport', 'reg_number', 'departure', 'destination', 'date_time_departure', 'date_time_destination', 'number_seats', 'number_carriage', 'price'
                  )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'number_passport': forms.TextInput(attrs={'class': 'form-control'}),
            'reg_number': forms.TextInput(attrs={'class': 'form-control'}),
            'departure': forms.TextInput(attrs={'class': 'form-control'}),
            'destination': forms.TextInput(attrs={'class': 'form-control'}),
            'date_time_departure': forms.TextInput(attrs={'class': 'form-control'}),
            'number_seats': forms.TextInput(attrs={'class': 'form-control'}),
            'number_carriage' : forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
        }