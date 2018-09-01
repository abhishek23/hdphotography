from django.shortcuts import render, HttpResponse
from .forms import ContactUsForm

def index(request):
	if request.method == 'POST':
		contactUsForm = ContactUsForm(request.POST)
	else:
		contactUsForm = ContactUsForm()
	context = {'form': contactUsForm}
	return render(request, 'contactus/contactus.html', context)
