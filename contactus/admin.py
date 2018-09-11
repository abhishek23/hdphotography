from django.contrib import admin
from .models import ContactUs, MyDetails

class ContactUsAdmin(admin.ModelAdmin):
	list_display = ('name', 'is_done')
	ordering = ('is_done',)

admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(MyDetails)