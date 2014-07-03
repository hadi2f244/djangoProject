from django.conf.urls import patterns,include,url


urlpatterns = patterns('',
    url(r'^$','blog.category.views.categories'),
    url(r'^all/$','blog.category.views.categories'),
    url(r'^get/(?P<category_id>\d+)/$','blog.category.views.category'),
)
