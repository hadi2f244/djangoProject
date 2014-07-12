__author__ = 'alireza'

from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from blog.models import Blog

class registerForm(ModelForm):
     #blog_need = forms.CharField(widget= forms.CheckboxInput, label=("I want a blog"))
     class Meta:
         model = User
         fields = ['username', 'password', 'email', 'first_name', 'last_name']



class RegBlog(ModelForm):
    class Meta :
        model = Blog
        fields = ["domain", "name"]