from django.forms import ModelForm
from models import Article,Comment
from tinymce.widgets import TinyMCE
from django import forms

############################################################################################

class ArticleForm(ModelForm): # it must convert to forms.Form for better speed
	#content = forms.CharField( widget=MarkdownWidget() )	
	body = forms.CharField(widget=TinyMCE(attrs={'cols': 70, 'rows': 20}))
	class Meta:
		model=Article
		fields= ('title','body','pub_date')

############################################################################################

class CommentForm(forms.Form):
	#body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
	writer = forms.CharField(max_length = 100)
	body = forms.CharField(widget=forms.Textarea)
