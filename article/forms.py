from django.forms import ModelForm
from models import Article,Comment
from tinymce.widgets import TinyMCE
from django import forms

#from django_markdown.widgets import MarkdownWidget
class ArticleForm(ModelForm):
	#content = forms.CharField( widget=MarkdownWidget() )	
	body = forms.CharField(widget=TinyMCE(attrs={'cols': 70, 'rows': 20}))
	class Meta:
		model=Article
		fields= ('title','body','pub_date')
	
class CommentForm(ModelForm):
	#body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
	class Meta:
		model=Comment
		fields=('writer','body')