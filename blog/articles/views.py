# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from articles.models import Article

def articles(request):
    entries = Article.objects.all().order_by("-date")
    return render(request, 'index.html', locals())