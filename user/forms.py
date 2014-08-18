
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from blog.models import Blog
from user.models import MyUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import ugettext_lazy as _



class registerForm(ModelForm):#forms.Form):
     #blog_need = forms.CharField(widget= forms.CheckboxInput, label=("I want a blog"))
     class Meta:
         model = MyUser
         #fields = ['username', 'email' ,'password']        THIS IS FOR CUSTOMIZING
         #fields = ['username', 'email' ,'password', 'aboutme']#, 'email', 'first_name', 'last_name']
         fields = ['username', 'email' , 'password', 'aboutme']#, 'email', 'first_name', 'last_name']



class RegBlog(ModelForm):
    class Meta :
        model = Blog
        fields = ["domain", "name"]


class loginForm(ModelForm):
    class Meta:
        model = MyUser
        fields = ['username', 'password']

class resetForm(forms.Form):
    email = forms.EmailField(label=_('email'))

class UserCreationForm(forms.ModelForm):
    """A form for creating new user. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Password confirmation'), widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('username', 'email', 'aboutme')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class reset_password_form(forms.Form):
    password1 = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Password confirmation'), widget=forms.PasswordInput)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2