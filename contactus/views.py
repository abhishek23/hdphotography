from django.shortcuts import render, HttpResponse
from .forms import ContactUsForm
from .models import MyDetails

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
	myDetails = MyDetails.objects.get(pk=1)
	context.update({'form': contactUsForm, 'myDetails': myDetails})
	return render(request, 'contactus/contactus.html', context)