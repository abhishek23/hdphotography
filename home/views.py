from django.shortcuts import render
from django.http import HttpResponse
from . import models

def index(request):
	slidingImages = models.HomePageSlider.objects.all()
	context = {'slidingImages': slidingImages}
	return render(request, 'home/index.html', context)

def weOffer(request):
	return render(request, 'home/we_offer.html')