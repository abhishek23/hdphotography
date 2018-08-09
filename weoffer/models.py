from django.db import models

class Event(models.Model):
	name = models.CharField(max_length=20)
	thumbnail = models.ImageField(upload_to='event_thumbnails')

	def __str__(self):
		return self.name

class EventImage(models.Model):
	image = models.ImageField(upload_to='event_images')
	event_id = models.ForeignKey(Event, related_name='images', on_delete=models.CASCADE)