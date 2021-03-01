from django.urls import path
from shoppingmodule.views import viewhome,viewaboutus
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', viewhome),
    url(r'^viewaboutus/$', viewaboutus),
]