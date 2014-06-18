from django.conf.urls import patterns,include,url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
	url(r'^$','views.fronEnd.article.articles'),
	url(r'^all/$','views.fronEnd.article.articles'),
	url(r'^get/(?P<article_id>\d+)/$','views.fronEnd.article.article'),
	url(r'^language/(?P<language>[a-z\-]+)/$','views.fronEnd.article.language'),
	url(r'^create_article/$','views.fronEnd.article.create_article'),
	url(r'^edit/(?P<article_id>\d+)/$','views.fronEnd.article.edit_article'),
	#url(r'^like/(?P<article_id>\d+)/$','article.views.like_article'),
)

urlpatterns += staticfiles_urlpatterns()