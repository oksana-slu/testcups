from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^contact/$', "contact.views.contact"),
    (r'^admin/', include(admin.site.urls)),
)
