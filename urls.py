from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'', include("testcups.contact.urls")),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}, name='auth_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='auth_logout'),
    (r'^admin/', include(admin.site.urls)),
)
