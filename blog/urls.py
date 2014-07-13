from django.conf.urls import patterns, include, url
from django.contrib import admin
from dajaxice.core import dajaxice_autodiscover, dajaxice_config


####dajaxice must be in main urls.py file!
admin.autodiscover()
dajaxice_autodiscover()

urlpatterns = patterns('',
    url(r'^articles/',include('blog.article.urls')),
    url(r'^categories/',include('blog.category.urls')),
    url(r'^$', 'blog.views.home'),
    #url(r'^', 'blog.views.home'),
    url(r'^home/', 'blog.views.home'),
    url(r'^admin/',include(admin.site.urls)),   
    #url(r'^accounts/login/$','djangoBlog.views.login'),
    #url(r'^accounts/login/$','blog.views.login'),
    #url(r'^accounts/logout/$','blog.views.logout'),
    #url(r'^accounts/register/$','blog.views.register_user'),
    #url(r'^markdown/', include( 'django_markdown.urls')),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'^search/', include('haystack.urls')),
    url(r'^administrator/',include('blog.backEnd.urls')),

)


###### must check urls without capatalized ! with or without last slash and ...