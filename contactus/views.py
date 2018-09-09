from django.shortcuts import render, HttpResponse
from .forms import ContactUsForm

def index(request):
	context = {}
	if request.method == 'POST':
		print("request: ", request)
		contactUsForm = ContactUsForm(request.POST)
		if contactUsForm.is_valid():
			contactUsForm.save()
			contactUsForm = ContactUsForm()
			context.update({'saved': True})
	else:
		contactUsForm = ContactUsForm()
	context.update({'form': contactUsForm})
	return render(request, 'contactus/contactus.html', context)