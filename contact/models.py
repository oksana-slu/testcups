from django.db import models
from django.forms import ModelForm


class Contact(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(blank=True, max_length=100)
    birth = models.DateField(blank=True, null=True)
    bio = models.TextField(blank=True)
    email = models.EmailField(max_length=75)
    jabber = models.CharField(blank=True, max_length=100)
    skype = models.CharField(blank=True, max_length=100)
    other_contacts = models.TextField(blank=True)

    def __unicode__(self):
        return self.name
        
        
class ContactForm(ModelForm):
    class Meta:
        model = Contact

