from django.shortcuts import render
from . import models

def divideListInChunks(listToDivide, chunkSize):
	for i in range(0, len(listToDivide), chunkSize):
		yield listToDivide[i: i+chunkSize]

def index(request):
	events = models.Event.objects.all().order_by('sequence')
	eventSetOfThree = [each for each in divideListInChunks(events, 3)]
	print(eventSetOfThree)
	return render(request, 'weoffer/weoffer.html', {'eventRows': eventSetOfThree})

def slider(request):
	events = models.Event.objects.all().order_by('sequence')
	return render(request, 'weoffer/weoffer_slider.html', {'events': events})

def eventDetail(request, eventId):
	event = models.Event.objects.prefetch_related('images').get(pk=eventId)
	return render(request, 'weoffer/event_detail.html', {'event': event})

def stories(request, featuredId):
	featured = models.Featured.objects.prefetch_related('images').get(pk=featuredId)
	return render(request, 'weoffer/stories.html', {'featured': featured})