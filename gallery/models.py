from django.db import models

class GalleryColumn(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

class GalleryImage(models.Model):
	columnId = models.ForeignKey(GalleryColumn, related_name='images', on_delete=models.CASCADE)
	image = models.ImageField(upload_to='gallery')
	sequence = models.IntegerField()

	class Meta:
		ordering = ['sequence']