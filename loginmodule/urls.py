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

    #reset password urls
    path('reset_password/',
    auth_views.PasswordResetView.as_view(template_name = 'passwordreset.html'),
    name='reset_password'),

    path('reset_password_sent/',
    auth_views.PasswordResetDoneView.as_view(template_name = 'passwordresetsent.html'),
    name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name = 'resetpasswordform.html'),
    name='password_reset_confirm'),

    path('reset_password_complete/',
    auth_views.PasswordResetCompleteView.as_view(template_name = 'resetpasswordcomplete.html'),
    name='password_reset_complete'),
]