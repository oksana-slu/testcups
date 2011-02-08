from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'', include("testcups.contact.urls")),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}, name='auth_login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='auth_logout'),
    (r'^admin/', include(admin.site.urls)),    
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^%s(.*)$' % settings.MEDIA_URL[1:],
         'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),         
    )
