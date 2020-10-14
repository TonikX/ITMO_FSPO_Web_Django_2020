from django import forms
from django.db import models
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import *


class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['RideId', 'DepartureTime', 'ArrivalTime', 'StartAt', 'FinishAt']
        widgets = {
            'RideId': forms.TextInput(attrs={'class': 'form-control'}),
            'DepartureTime': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'ArrivalTime': forms.DateTimeInput(attrs={'class': 'form-control'}),
            'StartAt': forms.TextInput(attrs={'class': 'form-control'}),
            'FinishAt': forms.TextInput(attrs={'class': 'form-control'}),
        }


# from Railway.forms import TrainForm   max_length=150,unique=True


class TrainForm(forms.ModelForm):
    # Train_ID = forms.IntegerField()
    # TrainName = forms.CharField(max_length=150, db_index=True)
    # TrainType = forms.CharField(max_length=150, db_index=True)
    # carCount = forms.IntegerField(max_length=150, db_index=True)
    # Train_ID.widget.attrs.update({'class':'form-control'})
    class Meta:
        model = Train
        fields = ['Train_ID', 'TrainName', 'TrainType', 'carCount', 'ScheduleID']
        widgets = {
            'Train_ID': forms.TextInput(attrs={'class': 'form-control'}),
            'TrainName': forms.TextInput(attrs={'class': 'form-control'}),
            'TrainType': forms.TextInput(attrs={'class': 'form-control'}),
            'carCount': forms.TextInput(attrs={'class': 'form-control'}),
            'ScheduleID': forms.Select(attrs={'class': 'form-control'}),
        }
    #   trainImg = models.ImageField(null = True,blank = True,upload_to ="images/")


class AuthUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] ='form-control'

    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if(commit):
            user.save()
        return user