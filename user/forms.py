from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

from blog.apps.blog.models import Blog
from user.models import MyUser


class RegBlog(ModelForm):
    class Meta :
        model = Blog
        fields = ["domain", "name"]

from django import forms

class loginForm(forms.Form):
    username = forms.CharField(max_length=50, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean_username(self):
        message = self.cleaned_data['username']
        num_words = len(message)
        if num_words == 0:
            raise forms.ValidationError("Username couldn't be empty")
        if num_words > 50:
            raise forms.ValidationError("Too Long username")
        return message

    def clean_password(self):
        message = self.cleaned_data['password']
        num_words = len(message)
        if num_words == 0:
            raise forms.ValidationError("Password couldn't be empty")
        return message


class resetForm(forms.Form):
    email = forms.EmailField(label=_('email'))

class UserCreationForm(forms.ModelForm):
    """A form for creating new user. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label=_('Password'), required= True ,widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Password confirmation'), required= True, widget=forms.PasswordInput)

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

    def clean_aboutme(self):
        message = self.cleaned_data['aboutme']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message


    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class reset_password_form(forms.Form):
    password1 = forms.CharField(label=_('Password'),  required= True,widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Password confirmation'), required= True, widget=forms.PasswordInput)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2


class profile_form(forms.ModelForm):
    """A form for creating new user. Includes all the required
    fields, plus a repeated password."""
    class Meta:
        model = MyUser
        fields = ('username', 'email', 'aboutme')

