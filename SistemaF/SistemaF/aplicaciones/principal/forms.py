from django import forms
from django.forms import widgets
from .models import Employees



class EmpleadoForms(forms.ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'
        widgets ={
            'birth_date':forms.SelectDateWidget(years=range(1945,2020)),
            'hire_date':forms.SelectDateWidget(years=range(1945,2020)),
        }
    def clean_gender(self):
        gender=self.cleaned_data['gender']
        l=['M',"F","f","m"]
        if (gender != "M" and gender!= "F" and gender!="f" and gender !="m"):
            raise forms.ValidationError("Campo Erroneo, Sólo admite M or F")
        return gender
    
    
