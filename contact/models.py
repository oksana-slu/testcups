from django.db import models


class Contact(models.Model):    
    name = models.CharField(max_length=100)
    last_name = models.CharField(blank=True, max_length=100)
    birth = models.DateField(blank=True)
    bio = models.TextField(blank=True)
    email = models.EmailField(max_length=75)
    jabber = models.CharField(blank=True, max_length=100)
    skype = models.CharField(blank=True, max_length=100)
    other_contacts = models.CharField(blank=True, max_length=200)
    
    def __unicode__(self):
        return self.name   
