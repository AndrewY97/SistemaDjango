from django import forms
from django.forms import widgets
from .models import Employees

class EmpleadoForms(forms.ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'
        widgets ={
            'birth_date':forms.SelectDateWidget(years=range(1945,2020)),
            'hire_date':forms.SelectDateWidget(years=range(1945,2020))
        }
    def clean_gender(self):
        gender=self.cleaned_data['gender']
        l=['M',"F","f","m"]
        if gender != "M" and gender!= "F" and gender!="f" and gender !="m":
            raise forms.ValidationError("Campo Erroneo, Sólo admite M or F")
        return gender
    
    def clean_first_name(self):
        fn=self.cleaned_data['first_name']
        if fn == "0" and fn == "1" and fn == "2" and fn == "3" and fn == "4" and fn == "5" and fn != "6":
            raise forms.ValidationError("Campo Erroneo, Sóllo se admiten LETRAS")
        return fn