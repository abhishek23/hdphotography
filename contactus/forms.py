from django.forms import ModelForm, Textarea
from .models import ContactUs

class ContactUsForm(ModelForm):
	class Meta:
		model = ContactUs
		fields = ('name', 'contactNo', 'emailId', 'query')
		widgets = {
			'query': Textarea(attrs={'cols': 80, 'rows': 5}),
		}