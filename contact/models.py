from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User


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


class Middleware(models.Model):
    user = models.ForeignKey(User, null=True)
    lang = models.CharField(max_length=100, null=True)
    path_info = models.CharField(max_length=100)
    remote_addr = models.CharField(max_length=100)
