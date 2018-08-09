from django.shortcuts import render
from . import models

def index(request):
	events = models.Event.objects.all()
	return render(request, 'weoffer/weoffer.html', {'events': events})

def eventDetail(request, eventId):
	event = models.Event.objects.prefetch_related('images').get(pk=eventId)
	return render(request, 'weoffer/event_detail.html', {'event': event})