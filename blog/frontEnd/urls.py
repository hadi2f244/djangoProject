from django.conf.urls import patterns,include,url


urlpatterns = patterns('',

    url(r'^$', 'blog.frontEnd.views.home'),
    #url(r'^', 'blog.views.home'),
    url(r'^home/', 'blog.frontEnd.views.home'),
    #articles:
	url(r'^articles/$','blog.frontEnd.views.articles'),
	url(r'^articles/all/$','blog.frontEnd.views.articles'),
	url(r'^articles/get/(?P<article_slug>\S+)/$','blog.frontEnd.views.article'),
	#url(r'^language/(?P<language>[a-z\-]+)/$','blog.article.views.language'),
	#url(r'^like/(?P<article_id>\d+)/$','article.views.like_article'),
    url(r'^articles/archive/(?P<year>[\d]+)/$', 'blog.frontEnd.views.dateYearArchive'),
    url(r'^articles/archive/(?P<year>[\d]+)/(?P<month>[\d]+)/$', 'blog.frontEnd.views.dateMonthArchive'),
    url(r'^articles/archive/(?P<year>[\d]+)/(?P<month>[\d]+)/(?P<day>[\d]+)/$', 'blog.frontEnd.views.dateDayArchive'),
    #categories:
    url(r'^categories/$','blog.frontEnd.views.categories'),
    url(r'^categories/all/$','blog.frontEnd.views.categories'),
    url(r'^categories/get/(?P<category_id>\d+)/$','blog.frontEnd.views.category'),
)

