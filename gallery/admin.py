from django.contrib import admin
from .models import GalleryColumn, GalleryImage

class GalleryImageInline(admin.TabularInline):
	model = GalleryImage

class GalleryColumnAdmin(admin.ModelAdmin):
	inlines = [GalleryImageInline]
	class Meta:
		model = GalleryColumn

admin.site.register(GalleryColumn, GalleryColumnAdmin)
admin.site.register(GalleryImage)