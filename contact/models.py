from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Message
from django.contrib.sessions.models import Session
from django.db.models.signals import post_save, post_delete
from datetime import datetime


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
    user = models.ForeignKey(User, blank=True, null=True, related_name='loguser')
    lang = models.CharField(max_length=100, blank=True)
    path_info = models.CharField(max_length=100)
    remote_addr = models.CharField(max_length=100)
    priority = models.IntegerField(default=0)


EVENT_CHOICES = (
    ('create', 'create'),
    ('edit', 'edit'),
    ('delete', 'delete'),
    )


class ModelLog(models.Model):
    model_log = models.ForeignKey(ContentType, related_name='allmodels')
    object_id = models.IntegerField()
    event = models.CharField(max_length=6)
    stamp = models.DateTimeField(default=datetime.now())


EVENT_CHOICES_DICT = {None: 'delete',
                      True: 'create',
                      False: 'edit'}


def event_callback(sender, instance, **kwargs):
    if sender not in (ModelLog, Middleware, Message, Session):
        content_type = ContentType.objects.get_for_model(sender)
        ModelLog.objects.create(model_log=content_type,
                                object_id=instance.id,
                                event=EVENT_CHOICES_DICT[kwargs.get('created',
                                                                    None)])


post_save.connect(event_callback)
post_delete.connect(event_callback)
