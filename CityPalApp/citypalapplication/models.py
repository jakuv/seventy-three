# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

## creating a User Profile Model this is to create users and define them within the data base
class UserProfiles (models.Model):
    ## defining different user types for the model
    STUDENT = 'STU'
    BUSINESS = 'BUS'
    TOURIST = 'TOU'
    ## this is for the choices a new register can make
    USER_TYPE = ((STUDENT, 'Student'), (BUSINESS, 'Business'), (TOURIST,'Tourist'),)
    ## grabs information from our User Model
    user = models.OneToOneField(User)
    ## store description and usertype which will be used to determin what type of information will be given
    description = models.CharField (max_length=100, default="")
    usertype = models.CharField (max_length= 10, choices= USER_TYPE, default= STUDENT)
