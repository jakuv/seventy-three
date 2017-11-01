from django.conf.urls import url
from . import views
from django.contrib.auth.views import login ## import the ability to create a login form
##Hosing the URLS for the log in as well as the main page
urlpatterns = [
    url(r'^$', views.home), ## connect to the home page
    url(r'^login/$', login, {'template_name':'landingpage/index.html'})##connects to landing page which is also login page
    url[r'^register/$', views.register, name='register']
]
