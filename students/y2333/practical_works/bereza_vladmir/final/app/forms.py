from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from project import settings
from django.db.models.signals import post_save


class Vacancy_form(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['profession', 'busy_time', 'education', 'salary', 'information', 'id_employer']
        widgets = {
            'profession': forms.TextInput(attrs={'class': 'form-control'}),
            'busy_time': forms.TextInput(attrs={'class': 'form-control'}),
            'education': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.TextInput(attrs={'class': 'form-control'}),
            'information': forms.TextInput(attrs={'class': 'form-control'}),
            'id_user': forms.TextInput(attrs={'class': 'form-control'}),
        }


class Employer_form(UserCreationForm):
    name = forms.CharField()
    field_of_activity = forms.CharField()
    address = forms.CharField()
    information = forms.CharField()
    class Meta:
        model = User
        fields = ('name', 'field_of_activity', 'address', 'information', 'password1', 'password2')


class Summary_form(forms.ModelForm):
    class Meta:
        model = Summary
        fields = ['profession', 'busy_time', 'education', 'desired_salary', 'information', 'id_job_seeker']
        widgets = {
            'profession': forms.TextInput(attrs={'class': 'form-control'}),
            'busy_time': forms.TextInput(attrs={'class': 'form-control'}),
            'education': forms.TextInput(attrs={'class': 'form-control'}),
            'desired_salary': forms.TextInput(attrs={'class': 'form-control'}),
            'information': forms.TextInput(attrs={'class': 'form-control'}),
            'id_user': forms.TextInput(attrs={'class': 'form-control'}),
        }


class Job_seeker_form(UserCreationForm):
    email = forms.CharField()
    phone_number = forms.CharField()
    class Meta:
        model = User
        fields = ('email', 'phone_number', 'username', 'email', 'password1', 'password2', 'first_name', 'last_name')


class Response_form(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['id_summary', 'id_vacancy', 'total']
        widgets = {
            'id_summary': forms.TextInput(attrs={'class': 'form-control'}),
            'id_vacancy': forms.TextInput(attrs={'class': 'form-control'}),
            'total': forms.TextInput(attrs={'class': 'form-control'}),
        }
