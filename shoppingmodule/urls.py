from django.urls import path,re_path
from shoppingmodule.views import viewhome,viewaboutus,addtocart,viewcart
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', viewhome, name='viewhome'),
    url(r'^viewaboutus/$', viewaboutus, name='viewaboutus'),
    url(r'^addtocart/$', addtocart, name='addtocart'),
    url(r'^viewcart/$', viewcart, name='viewcart'),
]