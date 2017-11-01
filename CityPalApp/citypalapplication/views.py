# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from citypalapplication.forms import RegistrationForm #, RegForm
#from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def home(request):
    ## this view request allows the user to access the landing page
    return render(request, 'landingpage/home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('/citypalapplication/login')
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'landingpage/signup.html', args)
