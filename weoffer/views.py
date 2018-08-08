from django.shortcuts import render
from . import models

def index(request):
	events = models.Events.objects.all()
	return render(request, 'weoffer/weoffer.html', {'events': events})
