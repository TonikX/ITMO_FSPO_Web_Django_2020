from django import forms
from .models import *


class AddGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = [
            "name_game",
            "genre",
            "year",
            "developer_has_game",
            "price"
        ]


class AddDeveloperForms(forms.ModelForm):
    class Meta:
        model = Developer
        fields = [
            "name",
            "location",
        ]


class AddCDForms(forms.ModelForm):
    class Meta:
        model = CD
        fields = [
            "idcd",
            "date",
            "price",
            "game_id",
        ]


class AddCustomerForms(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            "name",
            "surname",
            "login",
            "id_customer",
        ]


class AddOrderForms(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "date",
            "id_customer",
            "Game_has_Order",
        ]