from django.forms import ModelForm
from testcups.contact.models import Contact
import settings
from django import forms


class CalendarWidget(forms.TextInput):
    class Media:
        js = ('/admin/jsi18n/',
              settings.ADMIN_MEDIA_PREFIX + 'js/core.js',
              settings.ADMIN_MEDIA_PREFIX + "js/calendar.js",
              settings.ADMIN_MEDIA_PREFIX + "js/admin/DateTimeShortcuts.js")
        css = {
            'all': (
                settings.ADMIN_MEDIA_PREFIX + 'css/widgets.css',
                )
        }

    def __init__(self, attrs={}):
        super(CalendarWidget, self).__init__(attrs={'class': 'vDateField',
                                                    'size': '10'})


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        widgets = {
            'birth': CalendarWidget
        }
