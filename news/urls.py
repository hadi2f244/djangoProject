from django.conf.urls import patterns,include,url


urlpatterns = patterns('',
	url(r'^$','news.views.newses'),
	url(r'^all/$','news.views.newses'),
	url(r'^get/(?P<news_id>\d+)/$','news.views.news'),
)
