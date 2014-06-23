from django.conf.urls import patterns,include,url


urlpatterns = patterns('',
    url(r'^$','category.views.categories'),
    url(r'^all/$','category.views.categories'),
    url(r'^get/(?P<category_id>\d+)/$','category.views.category'),
)
