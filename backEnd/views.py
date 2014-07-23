from django.shortcuts import render,render
from blog.models import Blog
from blog.forms import BlogForm
from news.models import News
from news.forms import NewsForm
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

    if userAuthenticated : # if the user was activated
        return HttpResponseRedirect('/administrator/dashBoard')

    elif (request.method == "GET"): #if user not loggedin and  the first time that page loaded we create csrf num
        return render(request,'main/backEnd/main/login.html', context)

    else: # the POST with username and pass came :
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('/administrator/dashBoard')

        else : #if invalid username and pass entered we recreate a csrf num
            context['invalid']=True
            return render(request,'main/backEnd/main/login.html',context)

#################################################################################################
def logout(request):
    userAuthenticated = request.user.is_authenticated() and request.user.is_superuser
    if userAuthenticated:
        auth.logout(request)
    return HttpResponseRedirect("/administrator")
#################################################################################################
@backEnd
def dashBoard(request,context):
    return render(request,'main/backEnd/main/dashBoard.html',context)
#################################################################################################
#################################################################################################
#Blogs:
@backEnd
def blogs(request,context):
    context['blogs'] = Blog.objects.all()
    return render(request,"main/backEnd/blog//blogs.html",context)
#################################################################################################
@backEnd
def blog(request,context,blog_id):
    context['blog'] = Blog.objects.get(user_id=blog_id)
    context['blogAdminUrl'] = "http://"+ context['blog'].domain +"."+ settings.SITE_NAME +"/administrator/dashBoard"
    return render(request,"main/backEnd/blog/blog.html",context)
################################################################################################
@backEnd
def blogDel(request,context,blog_id):
    Blog.objects.get(user_id=blog_id).delete()
    return HttpResponseRedirect("/administrator/blogs/all")
################################################################################################

@backEnd
def blogEdit(request,context,blog_id):
    #if blog with this blo_id doesn't exist ####

    lastBlog=Blog.objects.get(user_id=blog_id)#So we dont need to send blog.id to BlogForm that did in blogCreate views
    if lastBlog is None: # Is there any blog to edit!
        return HttpResponseRedirect("/administrator/blogs/all")

    if 'submitBlog' in request.POST: #make sure that user click save button
        blogForm = BlogForm(request.POST,instance=lastBlog) #to edit we set instance otherwise this create new blog
        if blogForm.is_valid():
            blogForm.save()
            return HttpResponseRedirect("/administrator/blogs/get/"+blog_id)
    else:# if user enter for first time So needed to show blog informations
        blogForm=BlogForm(instance=lastBlog)
    context['method']='blogEdit'
    context['blog_id']=blog_id
    context['form']=blogForm
    return render(request,'main/backEnd/blog/submit_blog.html',context)
################################################################################################
@backEnd
def blogCreate(request,context):

    if 'submitBlog' in request.POST: #means you click on submit button named createArticle in submit_article.html
        blogForm = BlogForm(request.POST)
        if blogForm.is_valid():
            return HttpResponseRedirect("/administrator/blogs/get/"+ str(blogForm.save().user_id))
    else:
        blogForm = BlogForm()#create a simple ArticleForm
    context['method']='blogCreate'
    context['form']=blogForm
    return render(request,'main/backEnd/blog/submit_blog.html',context)
################################################################################################
################################################################################################
#newses:

@backEnd
def newses(request,context):

    if 'deleteButton' in request.POST: #Delete button clicked!
        checked=request.POST.getlist("newsIdCheckes")
        if not len(checked):
            return HttpResponseRedirect("")
        for newsID in checked:
            News.objects.get(id=newsID).delete() #we must check the delete process correction ####
    elif 'HideButton' in request.POST: #Delete button clicked!
        checked=request.POST.getlist("newsIdCheckes")
        if not len(checked):
            return HttpResponseRedirect("")
        for newsID in checked:
            ob = News.objects.get(id=newsID)
            ob.hide = True
            ob.save()

    context['newses'] = News.objects.all()
    return render(request,"main/backEnd/news/newses.html",context)

#################################################################################################
@backEnd
def news(request,context,news_id):#just show the news
    context['news'] = News.objects.get(id=news_id)
    return render(request,"main/backEnd/news/news.html",context)
#################################################################################################
@backEnd
def newsDel(request,context,news_id):
    #if article with this news_id doesn't exist ####
    News.objects.get(id=news_id).delete() #we must check the delete process correction ####
    # after deletation a box must show that ####
    return HttpResponseRedirect("/administrator/newses/all")
################################################################################################
####w
@backEnd
def newsEdit(request,context,news_id):
    #if news with this news_id doesn't exist ####
    #
    lastNews=News.objects.get(id=news_id)#So we dont need to send blog.id to NewsForm that did in newsCreate views
    if lastNews is None: # Is there any article to edit!
        return HttpResponseRedirect("/administrator/newses/all")

    if 'submitNews' in request.POST: #make sure that user click save button
        newsForm = NewsForm(request.POST,instance=lastNews) #to edit we set instance otherwise this create new news
        if newsForm.is_valid():
            newsForm.save()
            return HttpResponseRedirect("/administrator/newses/get/"+news_id)
    else:# if user enter for first time So needed to show article informations
        newsForm=NewsForm(instance=lastNews)
    context['method']='newsEdit'
    context['news_id']=news_id
    context['form']=newsForm
    return render(request,'main/backEnd/news/submit_news.html',context)

################################################################################################
@backEnd
def newsCreate(request,context):

    if 'submitNews' in request.POST: #means you click on submit button named createNews in submit_news.html
        newsForm = NewsForm(request.POST)
        if newsForm.is_valid():
            return HttpResponseRedirect("/administrator/newses/get/"+str(newsForm.save().id))
    else:
        newsForm = NewsForm()#create a simple NewsForm
    context['method']='newsCreate'
    context['form']=NewsForm
    return render(request,'main/backEnd/news/submit_news.html',context)
#################################################################################################