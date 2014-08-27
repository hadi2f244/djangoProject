from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
admin.autodiscover()
urlpatterns = patterns('',
    #url(r'blog$',include('blog.urls')),
    url(r'^$', "mainProject.views.home"),
    url(r'^news/', include('new.urls')),
    url(r'^accounts/', include('user.urls')),
    url(r'^showblogs$', "mainProject.views.showBlogs"),
    #url(r'^administrator/', include('backEnd.urls')),
    # Examples:
    # url(r'^$', 'mainProject.views.home', name='home'),
    # url(r'^mainProject/', include('mainProject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),

)
urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
