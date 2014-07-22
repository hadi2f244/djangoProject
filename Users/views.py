# Create your views here.


from django import forms
from Users.forms import registerForm, RegBlog
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from blog.models import Blog
from Users.models import MyUser

def register(request):
    if request.method == 'POST':
        form = registerForm(request.POST)
        form1 = RegBlog(request.POST)
        if form.is_valid() and form1.is_valid():
            new_user = form.save()
            username = form.cleaned_data["username"]
            myuser = MyUser.objects.get(username = username)
            myuser.is_active = False
            myuser.save()
            test = form1.cleaned_data
            myblog = Blog.objects.create(user = myuser , domain = test["domain"] , name = test["name"])
            myblog.save()
            return HttpResponseRedirect("/accounts/register_complete/")
    else:
        form = registerForm()
        form1 = RegBlog()
    return render(request, "main/frontEnd/users/registration_form.html", {
        'form': form, 'form1' : form1
    })

def activition_complete(request, uidb36, token):
    myuser = MyUser.objects.get(username = token)
    if myuser.activation_key == uidb36 :
        myuser.is_active = True
        myuser.save()
        return render(request, "main/frontEnd/users/activation_complete.html")
    else :
        return HttpResponse("information is invalid please register correctlly")




