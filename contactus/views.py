from django.shortcuts import render, HttpResponse

def index(request):
	return HttpResponse("<h2> Contact Us! </h2>")
