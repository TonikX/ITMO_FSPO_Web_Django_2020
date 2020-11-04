from django import forms
from .models import *


class BoatForm(forms.ModelForm):
    class Meta:
        model = Boat
        fields = ['id', 'name']


class PatrolForm(forms.ModelForm):
    class Meta:
        model = Patrol
        fields = [
            'id',
            'name',
            'position',
            'exp',
            'age',
            'boat_id'
        ]


class PatrollingForm(forms.ModelForm):
    class Meta:
        model = Patrolling
        fields = [
            'date',
            'boat_id',
            'area_id',
            'count'
        ]
