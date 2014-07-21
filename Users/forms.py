__author__ = 'alireza'

from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from blog.models import Blog
from Users.models import MyUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

'''
class registerForm(ModelForm):#forms.Form):
     #blog_need = forms.CharField(widget= forms.CheckboxInput, label=("I want a blog"))
     class Meta:
         model = MyUser
         #fields = ['username', 'password', 'email', 'first_name', 'last_name']
         fields = ['email', 'date_of_birth' ,'password']#, 'email', 'first_name', 'last_name']



class RegBlog(ModelForm):
    class Meta :
        model = Blog
        fields = ["domain", "name"]
'''
'''
#CREATING A FORM FOR NORMAL USER WITHOUT INHERITANCE
class registerForm(ModelForm):#forms.Form):
     #blog_need = forms.CharField(widget= forms.CheckboxInput, label=("I want a blog"))
     class Meta:
         model = MyUser
         #fields = ['username', 'password', 'email', 'first_name', 'last_name']
         fields = ['email', 'date_of_birth' ,'password']#, 'email', 'first_name', 'last_name']



class RegBlog(ModelForm):
    class Meta :
        model = Blog
        fields = ["domain", "name"]
'''
class registerForm(ModelForm):#forms.Form):
     #blog_need = forms.CharField(widget= forms.CheckboxInput, label=("I want a blog"))
     class Meta:
         model = MyUser
         #fields = ['username', 'email' ,'password']        THIS IS FOR CUSTOMIZING
         fields = ['username', 'email' ,'password', 'aboutme']#, 'email', 'first_name', 'last_name']
     '''def save(self, *args, **kwargs):
      """
      Update the primary email address on the related User object as well.
      """
      u = self.instance.user
      u.activition_key = self.cleaned_data['email']
      u.save()
      profile = super(registerForm, self).save(*args,**kwargs)
      return profile
    '''

     '''
     def save(self, force_insert=False, force_update=False, commit=True):
        m = super(registerForm, self).save(commit=False)
        # do custom stuff

        if commit:
            m.save()
        return m
    '''

class RegBlog(ModelForm):
    class Meta :
        model = Blog
        fields = ["domain", "name"]
