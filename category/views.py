from django.shortcuts import render_to_response
from category.models import Category
from article.models import Article
from django.core.context_processors import csrf 
from django.http import HttpResponseRedirect
from djangoBlog.views import frontEnd # frontEnd is frontEnd decorator!

@frontEnd
def categories(request,context):
    #we show all the categories
    context['categories']=Category.objects.all()
    return  render_to_response('frontEnd/category/categories.html',context)

@frontEnd
def category(request,context,category_id=1):
    #we show the articles that this category contains
    context['category']=Category.objects.get(id=category_id)
    context['articles']=Article.objects.filter(category__id=category_id).distinct()
    return render_to_response('frontEnd/category/category.html',context)