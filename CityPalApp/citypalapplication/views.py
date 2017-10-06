# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    ## this view request allows the user to access the landing page
    return render(request, 'landingpage/home.html')
