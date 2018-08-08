from django.db import models

class Events(models.Model):
	name = models.CharField(max_length=20)
	thumbnail = models.ImageField(upload_to='events')
