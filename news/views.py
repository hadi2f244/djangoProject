from django.shortcuts import render
from news.models import News
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from mainProject.views import frontEnd
from django.utils.translation import ugettext_lazy as _
##################################################################################################################
@frontEnd
def newses(request,context):
    context['newses'] = News.objects.all()
    return render(request,'main/frontEnd/news/newses.html',context)
##################################################################################################################

@frontEnd
def news(request,context,news_id):
    context['news'] = News.objects.get(id=news_id)
    return render(request,'main/frontEnd/news/news.html',context)