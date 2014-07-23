from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	#url(r'blog$',include('blog.urls')),

    url(r'^$','backEnd.views.login'),
    url(r'^logout$','backEnd.views.logout'),
    url(r'^dashBoard$','backEnd.views.dashBoard'),
    #blogs:
    url(r'^blogs$','backEnd.views.blogs'),
    url(r'^blogs/all$','backEnd.views.blogs'),
    url(r'^blogs/get/(?P<blog_id>\d+)/$','backEnd.views.blog'),
    url(r'^blogs/del/(?P<blog_id>\d+)/$','backEnd.views.blogDel'),
    url(r'^blogs/edit/(?P<blog_id>\d+)/$','backEnd.views.blogEdit'),
    url(r'^blogs/blogCreate/$','backEnd.views.blogCreate'),
    #newses:
    url(r'^newses$','backEnd.views.newses'),
    url(r'^newses/all$','backEnd.views.newses'),
    url(r'^newses/get/(?P<news_id>\d+)/$','backEnd.views.news'),
    url(r'^newses/edit/(?P<news_id>\d+)/$','backEnd.views.newsEdit'),
    url(r'^newses/del/(?P<news_id>\d+)/$','backEnd.views.newsDel'),
    url(r'^newses/newsCreate/$','backEnd.views.newsCreate'),
   # url(r'^blogs$', 'backEnd.views.blogs'),
   # url(r'^admin$', include('backEnd.urls')),

)
