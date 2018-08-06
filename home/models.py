from django.db import models

class HomePageSlider(models.Model):
	slidingImage = models.ImageField(upload_to='home_images', blank=True)
	description = models.TextField()
