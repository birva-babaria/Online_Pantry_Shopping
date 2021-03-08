from shoppingmodule.views import viewhome,viewaboutus,addtocart,viewcart,removefromcart,buynow,cartbill,confirmorder,confirmorderb,viewconfirmorder,viewprofile,changeaddress,addnewaddress,changepassword,updatepassword
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
    url(r'^confirmorder/$', confirmorder, name='confirmorder'),
    url(r'^confirmorderb/$', confirmorderb, name='confirmorderb'),
    url(r'^viewconfirmorder/$', viewconfirmorder, name='viewconfirmorder'),
    url(r'^viewprofile/$', viewprofile, name='viewprofile'),
    url(r'^changeaddress/$', changeaddress, name='changeaddress'),
    url(r'^addnewaddress/$', addnewaddress, name='addnewaddress'),
    url(r'^changepassword/$', changepassword, name='changepassword'),
    url(r'^updatepassword/$', updatepassword, name='updatepassword'),
]