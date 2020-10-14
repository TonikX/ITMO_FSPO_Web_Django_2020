from django.forms import ModelForm
from .models import *


class AutoForm(ModelForm):
    """Форма ввода авто"""

    class Meta:
        model = Auto
        fields = (
            'mark', 'model', 'transmission', 'issue',
            'mileage', 'color', 'count_owners', 'gear',
            'description', 'engine', 'price'
        )


class MarkForm(ModelForm):
    """Форма ввода марки"""

    class Meta:
        model = Mark
        fields = (
            'title',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.save:
            self.fields['title'].required = True


class ModelForm(ModelForm):
    """Форма ввода марки"""

    class Meta:
        model = Model
        fields = (
            'title',
        )


class TransmissionForm(ModelForm):
    """Форма ввода марки"""

    class Meta:
        model = Transmission
        fields = (
            'title',
        )


class GearForm(ModelForm):
    """Форма ввода марки"""

    class Meta:
        model = Gear
        fields = (
            'title',
        )


class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
