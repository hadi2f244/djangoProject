from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()
dajaxice_autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'article.views.articles'),
	url(r'^admin/',include(admin.site.urls)),	
	url(r'^accounts/login/$','testD.views.login'),
	url(r'^accounts/auth/$','testD.views.auth_view'),
	url(r'^accounts/logout/$','testD.views.logout'),
	url(r'^accounts/loggedin/$','testD.views.loggedin'),
	url(r'^accounts/invalid_login/$','testD.views.invalid_login'),
	url(r'^articles/',include('article.urls')),
	url(r'^accounts/register/$','testD.views.register_user'),
	url(r'^accounts/register_success/$','testD.views.register_success'),
	#url(r'^markdown/', include( 'django_markdown.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += staticfiles_urlpatterns()
