# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from citypalapplication.models import UserProfiles, Locations

# Register your models here.
admin.site.register(UserProfiles)
admin.site.register(Locations)
