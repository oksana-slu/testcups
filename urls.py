from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', "contact.views.contact"),
    url(r'^middleware/$', "middleware.views.middleware"),
    (r'^admin/', include(admin.site.urls)),
)
