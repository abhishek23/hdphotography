from django.db import models

class ContactUs(models.Model):
	name = models.CharField(max_length=100)
	contactNo = models.CharField(max_length=20)
	emailId = models.CharField(max_length=254, blank=True)
	query = models.CharField(max_length=1000)