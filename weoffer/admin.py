from django.contrib import admin
from . import models


class EventImageInline(admin.TabularInline):
	model = models.EventImage

class EventAdmin(admin.ModelAdmin):
	inlines = [EventImageInline]
	class Meta:
		model = models.Event

admin.site.register(models.Event, EventAdmin)
admin.site.register(models.EventImage)

class FeaturedImagesInline(admin.TabularInline):
	model = models.FeaturedImages

class FeaturedAdmin(admin.ModelAdmin):
	inlines = [FeaturedImagesInline]
	class Meta:
		model = models.Featured

admin.site.register(models.Featured, FeaturedAdmin)
admin.site.register(models.FeaturedImages)