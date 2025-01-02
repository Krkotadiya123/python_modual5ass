from django import forms
from .models import *

class doctorform(forms.ModelForm):
    class Meta:
        model=doctor_tbl
        fields=['fullname','email','password','mobile','specialization','image','role']
        
class patientsform(forms.ModelForm):    
    class Meta:
        model=patient
        fields=['fullname','email','password','mobile','age','role']


class contactfrom(forms.ModelForm):
    class Meta:
        model=contact
        fields='__all__'

class appintmentfrom(forms.ModelForm):
    class Meta:
        model=appointmentabl
        fields='__all__'

class apform(forms.ModelForm):
    class Meta:
        model=appointmentabl
        fields=['name','email','number','age','Action']

class pass_form(forms.ModelForm):
    class Meta:
        model=doctor_tbl
        fields=['password']

class ppass_form(forms.ModelForm):
    class Meta:
        model=doctor_tbl
        fields=['password']


