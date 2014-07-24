from django.conf.urls import patterns,include,url


urlpatterns = patterns('',
	url(r'^$','new.views.news'),
	url(r'^all/$','new.views.news'),
	url(r'^get/(?P<new_id>\d+)/$','new.views.new'),
)
