from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.core.context_processors import csrf 
#from django.contrib.auth.forms import UserCreationForm
from forms import MyRegistrationForm
from functools import wraps
from blog.models import Blog
#account registeration

#http://ccbv.co.uk/projects/Django/1.6/django.views.generic.base/TemplateView/
#https://docs.djangoproject.com/en/dev/topics/class-based-views/intro/

##################################################################################
'''
class frontEnd1(TemplateView):
	#template_name =
	def get_context_data(self, **kwargs):
		context = super(frontEnd1, self).get_context_data(**kwargs)
		context['userAuthenticated']=self.request.user.is_authenticated
		context['user']=self.request.user
		return context
'''
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

##################################################################################
@frontEnd
def home(request,context):
    return render_to_response("blog/frontEnd/djangoBlog/welcome.html",context)
##################################################################################
'''
@frontEnd
def register_user(request,context):
	context.update(csrf(request))
	if request.method =="POST":	
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return render_to_response('blog/frontEnd/djangoBlog/register_success.html',context) #no need to create a new url like register_success just render that html is enough (url is /accounts/register)
	context['form'] = MyRegistrationForm()
	return render_to_response('blog/frontEnd/djangoBlog/register.html',context)

#account login views
@frontEnd
def login(request,context):
	context.update(csrf(request))
	if context['userAuthenticated']: # if the user was activated we redirect the url to loggedin 
		return HttpResponseRedirect('/home') 

	elif (request.method == "GET"): #if user not loggedin and  the first time that page loaded we create csrf num
		return render_to_response('frontEnd/djangoBlog/login.html' , context)

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
				return render_to_response('frontEnd/djangoBlog/loggedin.html',context)

		else : #if invalid username and pass entered we recreate a csrf num 
			error ="invalid"
			context['error']=error	
			return render_to_response('blog/frontEnd/djangoBlog/login.html',context)

##################################################################################
'''
'''
@frontEnd
def logout(request,context):
	auth.logout(request)
	context['userAuthenticated']=False #set userAuthenticated to False because we want to render the new page from here
	return render_to_response('blog/frontEnd/djangoBlog/logout.html',context)
'''

