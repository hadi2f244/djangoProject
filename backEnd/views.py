from django.shortcuts import render_to_response
from blog.article.models import Article, Comment
from blog.models import Blog
from blog.category.models import Category
from blog.article.forms import ArticleForm,CommentForm,CommentFormEdit #,ArticleForm_edit
from django.contrib import auth
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings #we need SITE_NAME
from functools import wraps
#from django.contrib.auth.forms import PasswordChangeForm
from blog.backEnd.forms import  profileForm

def backEnd(view):
	@wraps(view)
	def wrapper(request,*args,**kwargs):
	 	context={}#context is data that will be replace with template variable
	 	context['userAuthenticated']=request.user.is_authenticated() and request.user.is_superuser
		context['user']=request.user
        #context['blog']=blog.objects.get()
		return view(request,context,*args,**kwargs)
	return wrapper

#################################################################################################################
#account login views
def login(request):
    context={}
    userAuthenticated = request.user.is_authenticated() and request.user.is_superuser
    context.update(csrf(request))
    if userAuthenticated : # if the user was activated
        return HttpResponseRedirect('/administrator/dashBoard')

    elif (request.method == "GET"): #if user not loggedin and  the first time that page loaded we create csrf num
        return render_to_response('main/backEnd/main/login.html', context)

    else: # the POST with username and pass came :
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('/administrator/dashBoard')

        else : #if invalid username and pass entered we recreate a csrf num
            context['invalid']=True
            return render_to_response('main/backEnd/main/login.html',context)

#################################################################################################
def logout(request):
    userAuthenticated = request.user.is_authenticated() and request.user.is_superuser
    if userAuthenticated:
        auth.logout(request)
    return HttpResponseRedirect("/administrator")
#################################################################################################
@backEnd
def dashBoard(request,context):
    return render_to_response('main/backEnd/main/dashBoard.html',context)
#################################################################################################
#################################################################################################
#Blogs:
@backEnd
def blogs(request,context):
    context['blogs'] = Blog.objects.all()
    return render_to_response("main/backEnd/blog/blog/blogs.html",context)
#################################################################################################
@backEnd
def blog(request,context,blog_id):
    context['blog'] = Blog.objects.get(user_id=blog_id)
    context['blogAdminUrl'] = "http://"+ context['blog'].domain +"."+ settings.SITE_NAME +"/administrator/dashBoard"
    return render_to_response("main/backEnd/blog/blog/blog.html",context)
################################################################################################
@backEnd
def blogDel(request,context,blog_id):
    Blog.objects.get(user_id=blog_id).delete()
    return HttpResponseRedirect("/administrator/blogs/all")
################################################################################################
'''
@backEnd
def blogEdit(request,context,article_id):
    #if article with this article_id doesn't exist ####
    context.update(csrf(request))
    lastArticle=Article.objects.get(id=article_id,blog_id=request.blog.id)#So we dont need to send blog.id to ArticleForm that did in articleCreate views
    if lastArticle is None: # Is there any article to edit!
        return HttpResponseRedirect("/administrator/articles/all")

    if 'submitArticle' in request.POST: #make sure that user click save button
        articleForm = ArticleForm(request.blog.id,request.POST,instance=lastArticle) #to edit we set instance otherwise this create new article
        if articleForm.is_valid():
            articleForm.save()
            return HttpResponseRedirect("/administrator/articles/get/"+article_id)
    else:# if user enter for first time So needed to show article informations
        articleForm=ArticleForm(blog_id=request.blog.id,instance=lastArticle)
    context['method']='articleEdit'
    context['article_id']=article_id
    context['form']=articleForm
    return render_to_response('backEnd/article/submit_article.html',context)
################################################################################################
@backEnd
def blogCreate(request,context):
    context.update(csrf(request))
    if 'submitBlog' in request.POST: #means you click on submit button named createArticle in submit_article.html
        articleForm = ArticleForm(request.blog.id,request.POST)
        if articleForm.is_valid():
            article=articleForm.save(commit=False)
            article.blog_id=request.blog.id
            article.save()
            #print article.body
            return HttpResponseRedirect("/administrator/articles/get/"+str(article.id))
    else:
        articleForm = ArticleForm(request.blog.id)#create a simple ArticleForm
    context['method']='articleCreate'
    context['form']=articleForm
    return render_to_response('backEnd/article/submit_article.html',context)
'''