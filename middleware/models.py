from django.db import models
from django.contrib.auth.models import User


class Middleware(models.Model):
    user = models.ForeignKey(User, null=True)
    lang = models.CharField(max_length=100, null=True)
    path_info = models.CharField(max_length=100)
    remote_addr = models.CharField(max_length=100)
