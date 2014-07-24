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
    #news:
    url(r'^news$','backEnd.views.news'),
    url(r'^news/all$','backEnd.views.news'),
    url(r'^news/get/(?P<new_id>\d+)/$','backEnd.views.new'),
    url(r'^news/edit/(?P<new_id>\d+)/$','backEnd.views.newEdit'),
    url(r'^news/del/(?P<new_id>\d+)/$','backEnd.views.newDel'),
    url(r'^news/newCreate/$','backEnd.views.newCreate'),
   # url(r'^blogs$', 'backEnd.views.blogs'),
   # url(r'^admin$', include('backEnd.urls')),

)
