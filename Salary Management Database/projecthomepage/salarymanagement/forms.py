from django import forms
from .models import *

class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = ('firstname', 'lastname')

class EmployeeForm(forms.ModelForm):
    class Meta:
        models = Employee
        fields = '__all__'

class CityForm(forms.ModelForm):
    class Meta:
        models = City
        fields = '__all__'