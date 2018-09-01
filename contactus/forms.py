from django import forms
from django.forms import ModelForm
from .models import ContactUs

class ContactUsForm(ModelForm):
	class Meta:
		model = ContactUs
		fields = ['name', 'contactNo', 'emailId', 'query']
		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-input'}),
			'contactNo': forms.TextInput(attrs={'class': 'form-input'}),
			'emailId': forms.TextInput(attrs={'class': 'form-input'}),
			'query': forms.TextInput(attrs={'class': 'form-input'}),
		}