from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'', include("testcups.contact.urls")),
    (r'^admin/', include(admin.site.urls)),
)
