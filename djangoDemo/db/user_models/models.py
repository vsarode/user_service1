# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import models


# Create your models here.
class User(models.Model):
    userid = models.CharField(max_length=255, primary_key=True)
    fname = models.CharField(max_length=1024, null=True)
    mname = models.CharField(max_length=1024, null=True)
    lname = models.CharField(max_length=1024, null=True)
    phone = models.CharField(max_length=12, null=True)
    password = models.CharField(max_length=1024)
    created_on = models.DateTimeField(auto_now=True)
    logins = models.ManyToManyField('Login', related_name='user_logins')


class Login(models.Model):
    user = models.ForeignKey(User)
    token = models.CharField(max_length=70, default=str(uuid.uuid4()),
                             primary_key=True)
    created_on = models.DateTimeField(auto_now=True)
    loggedout_time = models.DateTimeField(null=True)
    is_logged_in = models.BooleanField(default=True)
