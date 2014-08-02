from django.shortcuts import render,render
from blog.models import Blog
from blog.forms import BlogForm
from new.models import New
from new.forms import NewForm
from django.contrib import auth
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings #we need SITE_NAME
from functools import wraps
from django.utils.translation import ugettext as _
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
    context['blog'] = Blog.objects.get(id=blog_id)
    context['blogAdminUrl'] = "http://"+ context['blog'].domain +"."+ settings.SITE_NAME +"/administrator/dashBoard"
    return render(request,"main/backEnd/blog/blog.html",context)
################################################################################################
@backEnd
def blogDel(request,context,blog_id):
    Blog.objects.get(id=blog_id).delete()
    return HttpResponseRedirect("/administrator/blogs/all")
################################################################################################

@backEnd
def blogEdit(request,context,blog_id):
    #if blog with this blo_id doesn't exist ####

    lastBlog=Blog.objects.get(id=blog_id)#So we dont need to send blog.id to BlogForm that did in blogCreate views
    if lastBlog is None: # Is there any blog to edit!
        return HttpResponseRedirect("/administrator/blogs/all")

    if 'submitBlog' in request.POST: #make sure that user click save button
        blogForm = BlogForm(request.POST,instance=lastBlog) #to edit we set instance otherwise this create new blog
        if blogForm.is_valid():
            lastBlog.delete()
            new_blog=blogForm.save()
            print "ohhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
            print new_blog
            return HttpResponseRedirect("/administrator/blogs/get/"+new_blog.id)
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
            return HttpResponseRedirect("/administrator/blogs/get/"+ str(blogForm.save().id))
    else:
        blogForm = BlogForm()#create a simple ArticleForm
    context['method']='blogCreate'
    context['form']=blogForm
    return render(request,'main/backEnd/blog/submit_blog.html',context)
################################################################################################
################################################################################################
#news:

@backEnd
def news(request,context):

    if 'deleteButton' in request.POST: #Delete button clicked!
        checked=request.POST.getlist("newIdCheckes")
        if not len(checked):
            return HttpResponseRedirect("")
        for newID in checked:
            New.objects.get(id=newID).delete() #we must check the delete process correction ####
    elif 'HideButton' in request.POST: #Delete button clicked!
        checked=request.POST.getlist("newIdCheckes")
        if not len(checked):
            return HttpResponseRedirect("")
        for newID in checked:
            ob = New.objects.get(id=newID)
            ob.hide = True
            ob.save()

    context['news'] = New.objects.all()
    return render(request,"main/backEnd/new/news.html",context)

#################################################################################################
@backEnd
def new(request,context,new_id):#just show the new
    context['new'] = New.objects.get(id=new_id)
    return render(request,"main/backEnd/new/new.html",context)
#################################################################################################
@backEnd
def newDel(request,context,new_id):
    #if article with this news_id doesn't exist ####
    New.objects.get(id=new_id).delete() #we must check the delete process correction ####
    # after deletation a box must show that ####
    return HttpResponseRedirect("/administrator/news/all")
################################################################################################
####w
@backEnd
def newEdit(request,context,new_id):
    #if new with this new_id doesn't exist ####
    #
    lastNew=New.objects.get(id=new_id)#So we dont need to send blog.id to NewForm that did in newCreate views
    if lastNew is None: # Is there any article to edit!
        return HttpResponseRedirect("/administrator/news/all")

    if 'submitNew' in request.POST: #make sure that user click save button
        newForm = NewForm(request.POST,instance=lastNew) #to edit we set instance otherwise this create new news
        if newForm.is_valid():
            newForm.save()
            return HttpResponseRedirect("/administrator/news/get/"+new_id)
    else:# if user enter for first time So needed to show article informations
        newForm=NewForm(instance=lastNew)
    context['method']='newEdit'
    context['new_id']=new_id
    context['form']=newForm
    return render(request,'main/backEnd/new/submit_new.html',context)

################################################################################################
@backEnd
def newCreate(request,context):

    if 'submitNew' in request.POST: #means you click on submit button named createNew in submit_new.html
        newForm = NewForm(request.POST)
        if newForm.is_valid():
            return HttpResponseRedirect("/administrator/news/get/"+str(newForm.save().id))
    else:
        newForm = NewForm()#create a simple NewForm
    context['method']='newCreate'
    context['form']=NewForm
    return render(request,'main/backEnd/new/submit_new.html',context)
#################################################################################################