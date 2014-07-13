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
   # url(r'^blogs$', 'backEnd.views.blogs'),
   # url(r'^admin$', include('backEnd.urls')),

)
