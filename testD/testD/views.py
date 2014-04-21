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
