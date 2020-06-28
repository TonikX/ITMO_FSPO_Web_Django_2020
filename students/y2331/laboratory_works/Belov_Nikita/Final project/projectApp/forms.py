from django import forms
import datetime
from projectApp.models import ExtendedUserModel, Voyage, Crews, Trawlers, Awards, FishOperation
from django.db import models


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegForm(forms.ModelForm):
    class Meta:
        model = ExtendedUserModel
        fields = ['username', 'first_name', 'last_name', 'b_day', 'job_type', 'password']

    password_confirmation = forms.CharField(required=True)



class VoyageForm(forms.ModelForm):
    class Meta:
        model = Voyage
        fields = ['startDate', 'endDate', 'fishQty']


class AssignForm(forms.ModelForm):
    class Meta:
        model = Crews
        fields = ['tId', 'uId']


class TrawlerForm(forms.ModelForm):
    class Meta:
        model = Trawlers
        fields = ['id', 'name', 'prodDate']


class AwardForm(forms.ModelForm):
    class Meta:
        model = Awards
        fields = ['uId', 'awardSize']


class StockForm(forms.ModelForm):
    class Meta:
        model = FishOperation
        fields = [ 'date', 'price']
