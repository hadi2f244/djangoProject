from user.forms import registerForm, RegBlog
from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.models import Blog
from user.models import MyUser
from mainProject.views import frontEnd

@frontEnd
def register(request,context):
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
            return render(request,'main/frontEnd/user/registration_complete.html',context)
    else:
        context['form'] = registerForm()
        context['form1'] = RegBlog()
    return render(request, "main/frontEnd/user/registration_form.html",context)

@frontEnd
def activition_complete(request,context, uidb36, token):
    myuser = MyUser.objects.get(username = token)
    if myuser.activation_key == uidb36 :
        myuser.is_active = True
        myuser.save()
        return render(request, "main/frontEnd/user/activation_complete.html",context)
    else :
        return HttpResponse("information is invalid please register correctlly")




