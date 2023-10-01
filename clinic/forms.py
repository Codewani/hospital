from django import forms
from .models import *

class PatientForm(forms.ModelForm):
    class Meta:
        model = patient
        fields = '__all__'
        widgets = {
            'patient_id': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Patient ID'}),
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Name'}),
            'initials': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Initials'}),
            'sex': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Sex'}),
            'address': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Address'}),
            'post_code': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Post Code'}),
            'admission': forms.DateInput(attrs={'class':'form-control', 'placeholder': 'Admission Date (e.g., yyyy-mm-dd)', 'type': 'date'}),
            'DOB': forms.DateInput(attrs={'class':'form-control', 'placeholder': 'Date of Birth (e.g., yyyy-mm-dd)', 'type': 'date'}),
            'ward_id': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ward ID'}),
            'next_of_kin': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Next of Kin'}),
        }

class WardForm(forms.ModelForm):
    class Meta:
        model = ward
        fields = '__all__'
        widgets = {
            'ward_id': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ward ID'}),
            'ward_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ward Name'}),
            'number_beds': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Number of Beds'}),
            'nurse_in_charge': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Nurse in Charge'}),
            'ward_type': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Ward Type'}),
        }






