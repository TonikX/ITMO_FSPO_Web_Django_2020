from django.forms import ModelForm
from .models import *


class PatrolForm(ModelForm):
    class Meta:
        model = Patrol_result
        fields = ('date_patrol', 'vilorators_number')


class WaterAreaForm(ModelForm):
    class Meta:
        model = Patrol_water_area
        fields = (
            'water_area',
            'id_patrol_result',
        )

class PatrolmanForm(ModelForm):
    class Meta:
        model = Patrolman
        fields = (
            'name',
            'surname',
            'position',
            'date_birth',
            'experience',
            'begin_work',
        )