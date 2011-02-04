from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', include("testcups.contact.urls")),
    url(r'^middleware/$', "middleware.views.middleware"),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}, name='auth_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='auth_logout'),
    url(r'^edit_contact/$', "contact.views.edit_contact"),
    (r'^admin/', include(admin.site.urls)),
)
