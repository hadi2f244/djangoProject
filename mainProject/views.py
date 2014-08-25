from django.shortcuts import render
from functools import wraps
from new.models import New
from blog.models import Blog

def frontEnd(view):
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        context = {}  # context is data that will be replace with template variable
        return view(request, context, *args, **kwargs)
    return wrapper

@frontEnd
def home(request,context):
    context['news'] = New.objects.all()
    return render(request,'main/frontEnd/main/home.html',context)


@frontEnd
def showBlogs(request,context):
    context['blogs']=Blog.objects.all()
    return render(request,'main/frontEnd/main/blogs.html',context)
