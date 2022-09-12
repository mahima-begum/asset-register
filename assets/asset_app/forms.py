from dataclasses import fields
from pyexpat import model
from socket import fromshare
from tkinter.ttk import LabeledScale
from django import forms
from django.forms import ModelForm
from .models import Asset

class AssetForm(ModelForm):
    class Meta:
        model = Asset
        fields = ('name', 'type', 'brand', 'model_number', 'serial_number', 'registration_date', 'warranty', 'warranty_expiry', 'personal_device', 'location')
        labels = {'name': 'Name', 
            'type': 'Type',
            'brand': 'Brand', 
            'model_number': 'Model Number', 
            'serial_number': 'Serial Number',
            'registration_date': 'Registration Date', 
            'warranty': 'Warranty',
            'warranty_expiry': 'Warranty Expiry', 
            'personal_device': 'Personal Device', 
            'location': 'Location', 
            }
        widgets = {
			'name': forms.TextInput(attrs={'id':'name', 'class':'form-control', 'placeholder':'name'}),
			'type': forms.TextInput(attrs={'class':'form-control', 'placeholder':'type'}),
			'brand': forms.TextInput(attrs={'class':'form-control', 'placeholder':'brand'}),
			'model_number': forms.TextInput(attrs={'class':'form-control', 'placeholder':'model number'}),
			'serial_number': forms.TextInput(attrs={'class':'form-control', 'placeholder':'serial number'}),
			'registration_date': forms.DateInput(attrs={'class':'form-control', 'placeholder':'registration date', 'type':'date'}),
			'warranty': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'warranty'}),			
			'warranty_expiry': forms.DateInput(attrs={'class':'form-control', 'placeholder':'warranty expiry', 'type':'date'}),
			'personal_device': forms.CheckboxInput(attrs={'class':'form-control', 'placeholder':'personal device'}),
			'location': forms.TextInput(attrs={'class':'form-control', 'placeholder':'location'}),
		}


        