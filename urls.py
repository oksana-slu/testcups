from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', "contact.views.contact"),
    url(r'^middleware/$', "middleware.views.middleware"),
    url(r'^login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}, name='auth_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout',
        {'template_name': 'contact.html'}, name='auth_logout'),
    url(r'^edit_contact/$', "contact.views.edit_contact"),
    (r'^admin/', include(admin.site.urls)),
)
