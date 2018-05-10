from django import forms
from health_manager.models import Weight

class NewWeightForm(forms.ModelForm):
    class Meta():
        model = Weight
        fields = '__all__'
