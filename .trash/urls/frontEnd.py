
from django.conf.urls import patterns, include, url
from django.contrib import admin
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from frontEnds import *

urlpatterns = patterns('',
    #url(r'^articles/',include('urls.fronEnds.article')),
    url(r'^$', 'views.fronEnd.base.home'),
    url(r'^home/', 'views.fronEnd.base.home'),
    url(r'^admin/',include(admin.site.urls)),   
    #url(r'^accounts/login/$','djangoBlog.views.login'),
    url(r'^accounts/login/$','views.fronEnd.base.login'),
    url(r'^accounts/logout/$','views.fronEnd.base.logout'),
    url(r'^accounts/register/$','views.fronEnd.base.register_user'),
    #url(r'^markdown/', include( 'django_markdown.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'^search/', include('haystack.urls')),
    )

urlpatterns += staticfiles_urlpatterns()
