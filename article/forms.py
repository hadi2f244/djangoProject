from django.forms import ModelForm
from models import Article,Comment
from tinymce.widgets import TinyMCE
from django import forms

############################################################################################

class ArticleForm(forms.Form): # it must convert to forms.Form for better speed
	#content = forms.CharField( widget=MarkdownWidget() )	
	title = forms.CharField(max_length=200)
	body = forms.CharField(widget=TinyMCE(attrs={'cols': 70, 'rows': 20}))

############################################################################################
class ArticleForm_edit(forms.Form):
	title = forms.CharField(max_length=200)
	body = forms.CharField(widget=TinyMCE(attrs={'cols': 70, 'rows': 20}))
	pub_date = forms.DateTimeField()

############################################################################################

class CommentForm(forms.Form):
	#body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
	#writer = forms.CharField(max_length = 100)
	body = forms.CharField(widget=forms.Textarea)
