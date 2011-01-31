from django.contrib import admin
from testcups.middleware.models import Middleware


class MiddlewareAdmin(admin.ModelAdmin):
    list_display = ('user', 'path_info')


admin.site.register(Middleware, MiddlewareAdmin)
