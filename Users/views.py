# Create your views here.


from django import forms
from Users.forms import registerForm, RegBlog
from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.models import Blog
from django.contrib.auth.models import User as MyUser
#from Users.models import MyUser

def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            #user_trasfering = new_user
            #return HttpResponseRedirect("/accounts/register_complete/")
            return HttpResponseRedirect("/accounts/register_blog/" + form.cleaned_data["username"])
        #if form.is_valid and form.blog_need == True:
        #    return HttpResponseRedirect("/accounts/register_blog/")
    else:
        form = registerForm()
    return render(request, "registration/registration_form.html", {
        'form': form,
    })

#commit=False
def registerBlog(request, username):
    if request.method == 'POST':
        form = RegBlog(request.POST)
        if form.is_valid():
            #form.save()
            #form.user = user_trasfering
            #return HttpResponseRedirect("/accounts/Blog_registered/")
            myuser = MyUser.objects.get(username = username)
            test = form.cleaned_data
            myblog = Blog(user = myuser , domain = test["domain"] , name = test["name"])
            myblog.save()
            return HttpResponseRedirect("/accounts/register_complete/")
    else :
        form = RegBlog()
    return render(request, "registration/registration_Blog.html", {
        'form': form,
    })

'''def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            #user_trasfering = new_user
            #return HttpResponseRedirect("/accounts/register_complete/")
            return HttpResponseRedirect("/accounts/register_blog/" + form.cleaned_data["email"])
        #if form.is_valid and form.blog_need == True:
        #    return HttpResponseRedirect("/accounts/register_blog/")
    else:
        form = registerForm()
    return render(request, "registration/registration_form.html", {
        'form': form,
    })

#commit=False
def registerBlog(request, email):
    if request.method == 'POST':
        print "i am here        "
        form = RegBlog(request.POST)
        print "in form"
        if form.is_valid():
            #form.save()
            #form.user = user_trasfering
            #return HttpResponseRedirect("/accounts/Blog_registered/")
            myuser = MyUser.objects.get(email = email)
            test = form.cleaned_data
            myblog = Blog(user = myuser , domain = test["domain"] , name = test["name"])
            myblog.save()
            print "alireza snaaee"

            return HttpResponseRedirect("/accounts/register_complete/")
    else :
        form = RegBlog()
        print "hamidreza"
    return render(request, "registration/registration_Blog.html", {
        'form': form,
    })
'''