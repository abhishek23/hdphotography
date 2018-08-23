from django.db import models

class Event(models.Model):
	name = models.CharField(max_length=20)
	thumbnail = models.ImageField(upload_to='event_thumbnails')
	sequence = models.IntegerField(null=True)

	def __str__(self):
		return self.name

class EventImage(models.Model):
	image = models.ImageField(upload_to='event_images')
	event_id = models.ForeignKey(Event, related_name='images', on_delete=models.CASCADE)

class Featured(models.Model):
	name = models.CharField(max_length=100)
	event_id = models.ForeignKey(Event, related_name='featured_ids', on_delete=models.CASCADE)
	thumbnail = models.ImageField(upload_to='featured_thumbnails')
	coverImage = models.ImageField(upload_to='featured_cover_images')
	description = models.TextField()

	def __str__(self):
		return self.event_id.name + ': ' + self.name

class FeaturedImages(models.Model):
	featured_id = models.ForeignKey(Featured, related_name='images', on_delete=models.CASCADE)
	image = models.ImageField(upload_to='featured_images')

