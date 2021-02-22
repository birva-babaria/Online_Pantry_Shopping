from django.urls import path
from loginmodule.views import login, auth_view, logout, loggedin, invalidlogin, register, register_user
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    url(r'^login/$', login),
    url(r'^auth/$', auth_view),
    url(r'^registeruser/$', register_user),
    url(r'^register/$', register),
    url(r'^logout/$', logout),
    url(r'^loggedin/$', loggedin),
    url(r'^invalidlogin/$', invalidlogin),
]