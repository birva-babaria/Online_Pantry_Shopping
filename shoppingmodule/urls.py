from django.urls import path,re_path
from shoppingmodule.views import viewhome,viewaboutus,addtocart,viewcart,removefromcart,buynow,cartbill
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', viewhome, name='viewhome'),
    url(r'^viewaboutus/$', viewaboutus, name='viewaboutus'),
    url(r'^addtocart/$', addtocart, name='addtocart'),
    url(r'^viewcart/$', viewcart, name='viewcart'),
    url(r'^removefromcart/$', removefromcart, name='removefromcart'),
    url(r'^buynow/$', buynow, name='buynow'),
    url(r'^cartbill/$', cartbill, name='cartbill'),
]