from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import auth
from django.core.context_processors import csrf 
#from django.contrib.auth.forms import UserCreationForm
from forms import MyRegistrationForm
from django.views.generic.base import TemplateView
from functools import wraps

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
	 	context['userAuthenticated']=request.user.is_authenticated()
		context['user']=request.user
		return view(request,context,*args,**kwargs)
	return wrapper

##################################################################################
'''
class home(frontEnd):
    template_name = "welcome.html"
'''
@frontEnd
def home(request,context):
	return render_to_response("frontEnd/djangoBlog/welcome.html",context)
##################################################################################
@frontEnd
def register_user(request,context):
	context.update(csrf(request))
	if request.method =="POST":	
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return render_to_response('frontEnd/djangoBlog/register_success.html',context) #no need to create a new url like register_success just render that html is enough (url is /accounts/register)
	context['form'] = MyRegistrationForm()
	return render_to_response('frontEnd/djangoBlog/register.html',context)

'''

class register_user(frontEnd):
	template_name='register.html'
	#In get func we create new form and send it to the page 
	#In post func first we check the form validation if the form is not valid resend the new form to page
	def get(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		context.update(csrf(request))
		context['form']=MyRegistrationForm()
		return self.render_to_response(context)

	def post(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return render_to_response('register_success.html') #no need to create a new url like register_success just render that html is enough (url is /accounts/register)
		context.update(csrf(request))
		context['form']=MyRegistrationForm()
		return self.render_to_response(context)
'''
'''
def register_user(request):
	if request.method =="POST":	
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/register_success')

	args={}
	args.update(csrf(request))
	args['form'] = MyRegistrationForm()
	return render_to_response('register.html',args)
'''

##################################################################################

'''
class loggedin(frontEnd1):
	template_name="loggedin.html"
	def get(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		cotext['full_name']=request.user.username
		return self.render_to_response(context)
'''
##################################################################################

'''
@frontEnd
def login(request,context):
	context.update(csrf(request))
	if context['userAuthenticated'] : # if the user was activated we redirect the url to loggedin page (see frontEnd decorator)
			return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))#redirect to last page
	elif ('username' in request.POST) and ('password' in request.POST):#user send the user and pass to login 
			user=auth.authenticate(username=request.POST.get('username',''),password=request.POST.get('password',''))
			print "ohhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh"
			if user is not None: #if the user is ok 
				auth.login(request,user)
				if request.GET.__contains__('next'): #if the next variable(last page addr) we reverse to that page 
					return HttpResponseRedirect(request.GET['next'])
				else :
					return HttpResponseRedirect('/home')#render_to_response('loggedin.html',{'full_name':user.username})#now we render the loggedin.html with username the response that (notice : the url now is /accounts/login)
			else :#If invalid username or pass entered --> we imporved the error for that (send that to the login page in next lines)
				error ="invalid"
				context['error']=error
	return render_to_response('login.html',context)



class login(frontEnd1):
	template_name='login.html'
	def post(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		if request.user.is_active : # if the user was activated we redirect the url to loggedin page
			return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))#redirect to last page

		elif ('username' in request.POST) and ('password' in request.POST):#user send the user and pass to login 
			user=auth.authenticate(username=request.POST.get('username',''),password=request.POST.get('password',''))
			if user is not None: #if the user is ok 
				auth.login(request,user)
				if request.GET.__contains__('next'): #if the next variable(last page addr) we reverse to that page 
					return HttpResponseRedirect(request.GET['next'])
				else :
					return HttpResponseRedirect('/home')#render_to_response('loggedin.html',{'full_name':user.username})#now we render the loggedin.html with username the response that (notice : the url now is /accounts/login)
			else :#If invalid username or pass entered --> we imporved the error for that (send that to the login page in next lines)
				error ="invalid"
				context['error']=error

		#If invalid username or pass entered OR It's first time the page is loading (while the use not loggedin) --> we regenerate/generate a csrf num 
		context.update(csrf(request))	
		return self.render_to_response(context)
	def get(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		if request.user.is_active : # if the user was activated we redirect the url to loggedin page
			return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))#redirect to last page
		context.update(csrf(request))	
		return self.render_to_response(context)

'''

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
			return render_to_response('frontEnd/djangoBlog/login.html',context)

##################################################################################
'''
class logout(frontEnd1):
	template_name='logout.html'
	def get(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		auth.logout(request)
		return self.render_to_response(context)
'''
@frontEnd
def logout(request,context):
	auth.logout(request)
	context['userAuthenticated']=False #set userAuthenticated to False because we want to render the new page from here
	return render_to_response('frontEnd/djangoBlog/logout.html',context)












'''
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf 
#from django.contrib.auth.forms import UserCreationForm
from forms import MyRegistrationForm
#account registeration

def register_user(request):
	if request.method =="POST":	
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/register_success')

	args={}
	args.update(csrf(request))
	args['form'] = MyRegistrationForm()
	return render_to_response('register.html',args)

def register_success(request):
	#if request.REFERER=='http://127.0.0.1:8000/accounts/register/':
	#	print "ok"
	return render_to_response('register_success.html')

#account login views
def login(request):
	#print request.user.username
	if len(request.user.username) is 0:
		c = {}
		c.update(csrf(request))
		return render_to_response('login.html' , c)
	else:
		return HttpResponseRedirect('/accounts/loggedin')

def home(request):
	return render_to_response('welcome.html')

def auth_view(request):
	username=request.POST.get('username','')
	password=request.POST.get('password','')
	user=auth.authenticate(username=username,password=password) 

	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid_login')

def loggedin(request):
	if len(request.user.username) is not 0:
		return render_to_response('loggedin.html',
								{'full_name':request.user.username})
	else:
		return HttpResponseRedirect('/accounts/login')

def invalid_login(request):
	if len(request.user.username) is 0:
		return render_to_response('invalid_login.html')
	else:
		return HttpResponseRedirect('/accounts/loggedin')

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')

'''