from django.conf.urls import patterns,include,url


urlpatterns = patterns('',
	url(r'^$','blog.article.views.articles'),
	url(r'^all/$','blog.article.views.articles'),
	url(r'^get/(?P<article_id>\d+)/$','blog.article.views.article'),
	url(r'^language/(?P<language>[a-z\-]+)/$','blog.article.views.language'),
	#url(r'^like/(?P<article_id>\d+)/$','article.views.like_article'),
)
