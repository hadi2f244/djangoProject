from django.conf.urls import patterns,include,url


urlpatterns = patterns('',
    #url(r'^$','article.views.articles'),
    url(r'^$','backEnd.views.login'),
    url(r'^dashBoard$','backEnd.views.dashBoard'),
    #articles
    url(r'^articles$','backEnd.views.articles'),
    url(r'^articles/all$','backEnd.views.articles'),
    url(r'^articles/get/(?P<article_id>\d+)/$','backEnd.views.article'),
    url(r'^articles/del/(?P<article_id>\d+)/$','backEnd.views.articleDel'),
    url(r'^articles/edit/(?P<article_id>\d+)/$','backEnd.views.articleEdit'),
    url(r'^articles/articleCreate/$','backEnd.views.articleCreate'),
    #categories
    #url(r'^categories$','backEnd.views.categories'),
   # url(r'^categories/all/$','backEnd.views.categories'),
   # url(r'^categories/get/(?P<category_id>\d+)/$','backEnd.views.category'),
    )