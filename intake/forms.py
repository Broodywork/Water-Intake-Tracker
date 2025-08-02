from django import forms
from .models import WaterIntake

class WaterIntakeForm(forms.ModelForm):
    class Meta:
        model = WaterIntake
        fields = ['quantity_ml']
