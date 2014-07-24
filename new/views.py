from django.shortcuts import render
from new.models import New
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from mainProject.views import frontEnd
from django.utils.translation import ugettext_lazy as _
##################################################################################################################
@frontEnd
def news(request,context):
    context['new'] = New.objects.all()
    return render(request,'main/frontEnd/new/news.html',context)
##################################################################################################################

@frontEnd
def new(request,context,new_id):
    context['new'] = New.objects.get(id=new_id)
    return render(request,'main/frontEnd/new/new.html',context)