####reverse error must be solved!

from django import http
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
from blog.models import Blog
class SubdomainSet(object):
    def process_request(self, request):
        host=request.META['HTTP_HOST']
        pieces=host.split(".")
        domain=pieces[0]
        if pieces[1]=="com:8000" and pieces[0]=="test1" :
            request.urlconf=settings.ROOT_URLCONF['mainProject']
            return
        else:
            try:
                if request.blog and request.blog.domain==domain:
                    request.urlconf=settings.ROOT_URLCONF['blog']
                    return
                else:
                    blog = Blog.objects.get(domain=domain)
                    request.blog=blog
                    request.urlconf=settings.ROOT_URLCONF['blog']
                    return
            except AttributeError:#if we have no request.blog
                try:
                    blog = Blog.objects.get(domain=domain)
                    request.blog=blog
                    request.urlconf=settings.ROOT_URLCONF['blog']
                    return
                except ObjectDoesNotExist:
                    request.urlconf=settings.ROOT_URLCONF['mainProject']
                    return http.HttpResponseRedirect("http://test1.com:8000")
            except ObjectDoesNotExist:
                request.urlconf=settings.ROOT_URLCONF['mainProject']
                return http.HttpResponseRedirect("http://test1.com:8000")
