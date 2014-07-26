from django.shortcuts import render
from django.core.context_processors import csrf 

from functools import wraps
#account registeration

#http://ccbv.co.uk/projects/Django/1.6/django.views.generic.base/TemplateView/
#https://docs.djangoproject.com/en/dev/topics/class-based-views/intro/

##################################################################################

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
    context['blog_name']=request.blog.name
    return render(request,"blog/frontEnd/djangoBlog/home.html",context)
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


