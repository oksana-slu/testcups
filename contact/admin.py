from django.contrib import admin
from testcups.contact.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name')


admin.site.register(Contact, ContactAdmin)
