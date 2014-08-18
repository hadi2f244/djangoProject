from django.shortcuts import render
from functools import wraps


def home(request):
    return render(request, "test.html")


def frontEnd(view):
    @wraps(view)
    def wrapper(request, *args, **kwargs):
        context = {}  # context is data that will be replace with template variable
        return view(request, context, *args, **kwargs)
    return wrapper