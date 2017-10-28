# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from accounts.forms import SignUpForm

# Create your views here.
def home(request):
    ## this view request allows the user to access the landing page
    return render(request, 'landingpage/home.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landingpage/index.html')
    else:
        form = SignUpForm()

        args = {'form': form}
        return render{request, ''}
