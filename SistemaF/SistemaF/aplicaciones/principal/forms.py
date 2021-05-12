from django import forms
from .models import Employees

class EmpleadoForms(forms.ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'