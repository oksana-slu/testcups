from django.contrib import admin
from testcups.contact.models import Contact, Middleware, ModelLog


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name')


class MiddlewareAdmin(admin.ModelAdmin):
    list_display = ('user', 'path_info')


admin.site.register(Contact, ContactAdmin)
admin.site.register(Middleware, MiddlewareAdmin)
admin.site.register(ModelLog)
