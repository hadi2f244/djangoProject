__author__ = 'alireza'
from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url
from django.views.generic import TemplateView

from django.contrib.auth import views as auth_views

urlpatterns = patterns('',
                       url(r'^register/$', 'Users.views.register'),
                       url(r'^register_complete/$', TemplateView.as_view(template_name='registration/registration_complete.html')),
                       url(r'^register_blog/(?P<username>\w{0,50})/$', 'Users.views.registerBlog'),

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