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
admin.site.register(models.Featured)
admin.site.register(models.FeaturedImages)