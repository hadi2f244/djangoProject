from django.conf.urls import patterns,include,url
from django.contrib.auth.views import password_change,password_change_done

urlpatterns = patterns('',
    #url(r'^$','article.views.articles'),
    url(r'^$','blog.backEnd.views.login'),
    url(r'^logout$','blog.backEnd.views.logout'),
    url(r'^dashBoard$','blog.backEnd.views.dashBoard'),
    #articles
    url(r'^articles$','blog.backEnd.views.articles'),
    url(r'^articles/all','blog.backEnd.views.articles'),
    #r'^(?P<slug>\S+)$'
    url(r'^articles/get/(?P<article_slug>\S+)/$','blog.backEnd.views.article'),
    url(r'^articles/del/(?P<article_slug>\S+)/$','blog.backEnd.views.articleDel'),
    url(r'^articles/edit/(?P<article_slug>\S+)/$','blog.backEnd.views.articleEdit'),
    url(r'^articles/articleCreate/$','blog.backEnd.views.articleCreate'),
    #categories
    url(r'^categories$','blog.backEnd.views.categories'),
    url(r'^categories/all','blog.backEnd.views.categories'),
    url(r'^categories/categoryCreate/$','blog.backEnd.views.categoryCreate'),
    url(r'^categories/get/(?P<category_id>\d+)/$','blog.backEnd.views.category'),
    url(r'^categories/del/(?P<category_id>\d+)/$','blog.backEnd.views.categoryDel'),
    url(r'^categories/edit/(?P<category_id>\d+)/$','blog.backEnd.views.categoryEdit'),
    #comments
    url(r'^comments$','blog.backEnd.views.comments'),
    url(r'^comments/all','blog.backEnd.views.comments'),
    url(r'^comments/articles$','blog.backEnd.views.cArticles'),
    url(r'^comments/articles/all','blog.backEnd.views.cArticles'),
    url(r'^comments/articles/get/(?P<article_slug>\S+)/$','blog.backEnd.views.cArticle'),
    url(r'^comments/get/(?P<comment_id>\d+)/$','blog.backEnd.views.comment'),
    url(r'^comments/del/(?P<comment_id>\d+)/$','blog.backEnd.views.commentDel'),
    url(r'^comments/edit/(?P<comment_id>\d+)/$','blog.backEnd.views.commentEdit'),
    #url(r'^comments/commentCreate/$','backEnd.views.comment'),
    #profile
    url(r'^profile/','blog.backEnd.views.profile'),
    #url(r'^profile/passChange$','django.contrib.auth.views.password_change'),
    url(r'^profile/passChangeDone$','django.contrib.auth.views.password_change_done'),
    )