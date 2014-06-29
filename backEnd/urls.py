from django.conf.urls import patterns,include,url
from django.contrib.auth.views import password_change,password_change_done

urlpatterns = patterns('',
    #url(r'^$','article.views.articles'),
    url(r'^$','backEnd.views.login'),
    url(r'^logout$','backEnd.views.logout'),
    url(r'^dashBoard$','backEnd.views.dashBoard'),
    #articles
    url(r'^articles$','backEnd.views.articles'),
    url(r'^articles/all','backEnd.views.articles'),
    url(r'^articles/get/(?P<article_id>\d+)/$','backEnd.views.article'),
    url(r'^articles/del/(?P<article_id>\d+)/$','backEnd.views.articleDel'),
    url(r'^articles/edit/(?P<article_id>\d+)/$','backEnd.views.articleEdit'),
    url(r'^articles/articleCreate/$','backEnd.views.articleCreate'),
    #categories
    url(r'^categories$','backEnd.views.categories'),
    url(r'^categories/all','backEnd.views.categories'),
    url(r'^categories/categoryCreate/$','backEnd.views.categoryCreate'),
    url(r'^categories/get/(?P<category_id>\d+)/$','backEnd.views.category'),
    url(r'^categories/del/(?P<category_id>\d+)/$','backEnd.views.categoryDel'),
    url(r'^categories/edit/(?P<category_id>\d+)/$','backEnd.views.categoryEdit'),
    #comments
    url(r'^comments$','backEnd.views.comments'),
    url(r'^comments/all','backEnd.views.comments'),
    url(r'^comments/articles$','backEnd.views.cArticles'),
    url(r'^comments/articles/all','backEnd.views.cArticles'),
    url(r'^comments/articles/get/(?P<article_id>\d+)/$','backEnd.views.cArticle'),
    url(r'^comments/get/(?P<comment_id>\d+)/$','backEnd.views.comment'),
    url(r'^comments/del/(?P<comment_id>\d+)/$','backEnd.views.commentDel'),
    url(r'^comments/edit/(?P<comment_id>\d+)/$','backEnd.views.commentEdit'),
    #url(r'^comments/commentCreate/$','backEnd.views.comment'),
    #profile
    url(r'^profile/','backEnd.views.profile'),
    #url(r'^profile/passChange$','django.contrib.auth.views.password_change'),
    url(r'^profile/passChangeDone$','django.contrib.auth.views.password_change_done'),
    )