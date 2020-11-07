from django import forms
from .models import Driver, Offence, Judgement, Inspector, Car

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver

        fields = ["fio_driver", "birthday", "phone", "license_number", "address"]

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["brand", "model", "color", "pub_year", "date_reg", "license_plate", "driver"]

class InspectorForm(forms.ModelForm):
    class Meta:
        model = Inspector
        fields = ["fio_inspector", "num_inspector"]

class JudgementForm(forms.ModelForm):
    class Meta:
        model = Judgement
        fields = ["date_judgement", "time_judgement", "offence", "inspector", "car", "area"]

class OffenceForm(forms.ModelForm):
    class Meta:
        model = Offence
        fields = ["type", "fine", "term_deprivation"]

