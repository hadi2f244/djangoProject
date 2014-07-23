from django.shortcuts import render
from blog.category.models import Category
from blog.article.models import Article
from django.core.context_processors import csrf
from blog.views import frontEnd # frontEnd is frontEnd decorator!

@frontEnd
def categories(request,context):
    #we show all the categories
    context['categories']=Category.objects.filter(blog_id=request.blog.user_id)
    return  render(request,'frontEnd/category/categories.html',context)

@frontEnd
def category(request,context,category_id=1):
    #we show the articles that this category contains
    context['category']=Category.objects.get(id=category_id,blog_id=request.blog.user_id)
    context['articles']=Article.objects.filter(category__id=category_id,blog_id=request.blog.user_id).distinct()
    return render(request,'frontEnd/category/category.html',context)