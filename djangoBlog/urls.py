from django.conf.urls import patterns, include, url
from django.contrib import admin
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()
dajaxice_autodiscover()


urlpatterns = patterns('',
    url(r'^articles/',include('article.urls')),
    url(r'^categories/',include('category.urls')),
    url(r'^$', 'djangoBlog.views.home'),
    url(r'^home/', 'djangoBlog.views.home'),
    url(r'^admin/',include(admin.site.urls)),   
    #url(r'^accounts/login/$','djangoBlog.views.login'),
    url(r'^accounts/login/$','djangoBlog.views.login'),
    url(r'^accounts/logout/$','djangoBlog.views.logout'),
    url(r'^accounts/register/$','djangoBlog.views.register_user'),
    #url(r'^markdown/', include( 'django_markdown.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url(r'^search/', include('haystack.urls')),
    url(r'^administrator/',include('backEnd.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    )

urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


###### must check urls without capatalized ! with or without last slash and ...