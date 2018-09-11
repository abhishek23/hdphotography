from django.db import models
from django.core.exceptions import ValidationError


class ContactUs(models.Model):

	def validateContactNo(value):
		if not value.isdigit():
			raise ValidationError("Invalid Contact Number.")

	name = models.CharField(max_length=100)
	contactNo = models.CharField(max_length=20, validators=[validateContactNo])
	emailId = models.EmailField(max_length=254, blank=True)
	query = models.CharField(max_length=1000)
	is_done = models.BooleanField(verbose_name='Done', default=False)

	class Meta:
		verbose_name_plural = "Contact Us"


class MyDetails(models.Model):

	logoContactUs = models.ImageField(upload_to='my_details')
	mobileNos = models.CharField(max_length=30)
	emailId = models.EmailField(max_length=254)