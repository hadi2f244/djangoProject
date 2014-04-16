from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^article/$', include('articles.urls')),
    url(r'^accounts/login$','blog.views.login'),
    url(r'^accounts/auth$','blog.views.auth_view'),
    url(r'^accounts/logout$','blog.views.logout'),
    url(r'^accounts/loggedin','blog.views.loggedin'),
    url(r'^accounts/invalid$','blog.views.invalid_login'),
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
