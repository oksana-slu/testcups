from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('contact.views',
    url(r'^$', "contact", name='contact_home'),
    url(r'^middleware/$', "middleware", name='contact_middleware'),
    url(r'^edit_contact/$', "edit_contact", name='contact_edit'),
)
