from django.shortcuts import render, HttpResponse
from .models import GalleryColumn, GalleryImage

def index(request):
	galleryImages = GalleryColumn.objects.prefetch_related('images').all().order_by('id')
	print("------------------------------------")
	print(galleryImages)
	return render(request, 'gallery/gallery.html', {'imageColumns': galleryImages})
