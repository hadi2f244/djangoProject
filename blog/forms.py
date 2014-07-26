from django import forms
from blog.models import Blog
from django.contrib.auth.forms import UserCreationForm
from user.models import MyUser
from django.utils.translation import ugettext_lazy as _

class BlogForm(forms.ModelForm):
    #domain=forms.CharField(max_length=200)
    #name=forms.CharField(max_length=200)
    user=forms.ModelChoiceField(label=_('user'),queryset=MyUser.objects.all())
    class Meta:
        model= Blog
        fields = ['domain','name', 'user' ]


class MyRegistrationForm(UserCreationForm):
	email = forms.EmailField(required=True)
	class Meta:
		model=MyUser
		fields = ('username','email','password1','password2')
	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
