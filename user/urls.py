from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url

from django.views.generic import TemplateView

from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
    url(r'^register/$', 'user.views.register', name = 'account_register'),
    url(r'^(?P<uidb36>\b[0-9a-f]{5,40}\b)-(?P<token>\w{0,50})/activating/$', 'user.views.activition_complete'),
    url(r'^reset/$', 'user.views.reset_password', name = 'reset_password'),
    url(r'^login/$', 'user.views.login_func', name='login'),
    url(r'^(?P<key>\b[0-9a-f]{5,40}\b)-(?P<email>[\w.%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4})/setpassword/$', 'user.views.set_new_password'),
    url(r'^profile/$', 'user.views.profile', name='profile'),
    url(r'^logout/$', 'user.views.logout_view', name='logout'),



)

'''urlpatterns = patterns('',
                       url(r'^login/$',
                           auth_views.login,
                           {'template_name': 'registration/login.html'},
                           name='auth_login'),
                       url(r'^logout/$',
                           auth_views.logout,
                           {'template_name': 'registration/logout.html'},
                           name='auth_logout'),
                       url(r'^password/change/$',
                           auth_views.password_change,
                           name='auth_password_change'),
                       url(r'^password/change/done/$',
                           auth_views.password_change_done,
                           name='auth_password_change_done'),
                       url(r'^password/reset/$',
                           auth_views.password_reset,
                           name='auth_password_reset'),
                       url(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
                           auth_views.password_reset_confirm,
                           name='auth_password_reset_confirm'),
                       url(r'^password/reset/complete/$',
                           auth_views.password_reset_complete,
                           name='auth_password_reset_complete'),
                       url(r'^password/reset/done/$',
                           auth_views.password_reset_done,
                           name='auth_password_reset_done'),
                       )
                    '''