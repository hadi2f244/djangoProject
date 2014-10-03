from functools import wraps

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404
import jdatetime
from django.shortcuts import render
from blog.apps.article.models import Article
from blog.apps.category.models import Category
from blog.apps.comment.models import Comment
from blog.apps.blog.models import Blog
from blog.apps.comment.forms import CommentForm


def frontEnd(view):
	@wraps(view)
	def wrapper(request,*args,**kwargs):
	 	context={}#context is data that will be replace with template variable
	 	#context['userAuthenticated']=request.user.is_authenticated()
	 	context['log']="domainName: "+request.blog.domain
		#context['user']=request.user
        #context['blog']=blog.objects.get()
		return view(request,context,*args,**kwargs)
	return wrapper


##################################################################################################################
###Blog:
@frontEnd
def home(request,context):
    context['blog_name']=request.blog.name
    return render(request,"frontEnd/djangoBlog/home.html",context)

##################################################################################################################
###Articles:
@frontEnd
def articles(request,context):
    context['articles'] = request.blog.article_set.all()#Article.objects.filter(blog_id=request.blog.id)
    #context['articles'] = Article.objects.get(hide=True)
    return render(request,'frontEnd/article/articles.html',context)

##################################################################################################################

@frontEnd
def article(request,context,article_slug):
    context['article'] = request.blog.article_set.get(slug=article_slug)
    context['commnets'] = request.blog.comment_set.filter(article = context['article'])#article_id)
    if True :#context['userAuthenticated']:#see frontEnd decorator
        #################################
        #check commment create:
        if 'commentButton' in request.POST: #comment(create) button clicked!
            comment_form = CommentForm(request.POST) #if is valid --> save if not we create a new CommentForm with some error for user(like empty field and ...)
            if comment_form.is_valid():
                writer=request.POST['writer']
                body=request.POST['body']
                request.blog.comment_set.create(writer=writer,body=body,article=context['article'])
                return HttpResponseRedirect('') #just for reload the page and cleaning the fields
        else:
            comment_form=CommentForm() #create a simple CommentForm
            ##################################
    else :
        comment_form=None
    #set template variable:
    context['comment_form']=comment_form
    return render(request,'frontEnd/article/article.html',context)

##################################################################################################################

def language(request,language='en-gb'):
	response = HttpResponse("setting language to %s"% language)
	response.set_cookie('lang',language)
	request.session['lang'] = language
	return response


##################################################################################################################


'''def like_article(request,article_id):
	if article_id:
		article=Article.objects.get(id=article_id)
		count = article.likes
		count +=1
		article.likes = count
		# i must use csrf for likes,too
		article.save()
	return HttpResponseRedirect('/articles/get/%s'% article_id)
'''

    ###Archive:

@frontEnd
def dateYearArchive(request,context,year):
    year = int(year)
    if year%4==3 :
        day='30'
    else:
        day='29'
    context['articles']=request.blog.article_set.filter(pub_date__range=[str(year)+"-1-31",str(year)+"-12-"+day])
    context['date']=str(year)
    return render(request,'frontEnd/article/archive.html',context)


@frontEnd
def dateMonthArchive(request,context,year,month):
    year = int(year)
    month = int(month)
    if month<1 or month>12 :
        raise Http404
    YM=str(year)+"-"+str(month)+"-"
    context['articles']=request.blog.article_set.filter(pub_date__range=[YM+"1",YM+str(jdatetime.j_days_in_month[month-1])])
    context['date']=str(year) + "/" + str(month)
    return render(request,'frontEnd/article/archive.html',context)


@frontEnd
def dateDayArchive(request,context,year,month,day):
    year = int(year)
    month = int(month)
    day = int(day)
    if month<1 or month>12 or day<0 or day>31 :
        raise Http404
    context['articles']=request.blog.article_set.filter(pub_date=str(year)+'-'+str(month)+'-'+str(day))
    context['date']=str(year) + "/" + str(month) + "/" + str(day)
    return render(request,'frontEnd/article/archive.html',context)


###########################################################################################################################
###Category:
@frontEnd
def categories(request,context):
    #we show all the categories
    context['categories']=request.blog.category_set.all()
    return  render(request,'frontEnd/category/categories.html',context)

@frontEnd
def category(request,context,category_id=1):
    #we show the articles that this category contains
    context['category']=request.blog.category_set.get(id=category_id)
    context['articles']=request.blog.article_set.filter(category__id=category_id).distinct()
    return render(request,'frontEnd/category/category.html',context)




##################################################################################

##################################################################################
'''
@frontEnd
def register_user(request,context):

	if request.method =="POST":
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request,'blog/frontEnd/djangoBlog/register_success.html',context) #no need to create a new url like register_success just render that html is enough (url is /accounts/register)
	context['form'] = MyRegistrationForm()
	return render(request,'blog/frontEnd/djangoBlog/register.html',context)

#account login views
@frontEnd
def login(request,context):

	if context['userAuthenticated']: # if the user was activated we redirect the url to loggedin
		return HttpResponseRedirect('/home')

	elif (request.method == "GET"): #if user not loggedin and  the first time that page loaded we create csrf num
		return render(request,'frontEnd/djangoBlog/login.html' , context)

	else: # the POST with username and pass came :
		username=request.POST.get('username','')
		password=request.POST.get('password','')
		user=auth.authenticate(username=username,password=password)
		if user is not None:

			auth.login(request,user)
			if request.GET.__contains__('next'): #if the next variable(last page addr) we reverse to that page
				return HttpResponseRedirect(request.GET['next'])
			else :
				context['full_name']=user.username
				context['userAuthenticated']=True #set userAuthenticated to True because we want to render the new page from here
				context['user']=user
				return render(request,'frontEnd/djangoBlog/loggedin.html',context)

		else : #if invalid username and pass entered we recreate a csrf num
			error ="invalid"
			context['error']=error
			return render(request,'blog/frontEnd/djangoBlog/login.html',context)

##################################################################################
'''
'''
@frontEnd
def logout(request,context):
	auth.logout(request)
	context['userAuthenticated']=False #set userAuthenticated to False because we want to render the new page from here
	return render(request,'blog/frontEnd/djangoBlog/logout.html',context)
'''


