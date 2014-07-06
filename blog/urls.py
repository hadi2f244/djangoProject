from django.conf.urls import patterns, include, url
from django.contrib import admin
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

####dajaxice must be in main urls.py file!
admin.autodiscover()
dajaxice_autodiscover()

urlpatterns = patterns('',
    url(r'^articles/',include('blog.article.urls')),
    url(r'^categories/',include('blog.category.urls')),
    url(r'^$', 'blog.views.home'),
    url(r'^home/', 'blog.views.home'),
    url(r'^admin/',include(admin.site.urls)),   
    #url(r'^accounts/login/$','djangoBlog.views.login'),
    url(r'^accounts/login/$','blog.views.login'),
    url(r'^accounts/logout/$','blog.views.logout'),
    url(r'^accounts/register/$','blog.views.register_user'),
    #url(r'^markdown/', include( 'django_markdown.urls')),
    #url(r'^tinymce/', include('tinymce.urls')),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'^search/', include('haystack.urls')),
    url(r'^administrator/',include('blog.backEnd.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    )


urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


###### must check urls without capatalized ! with or without last slash and ...