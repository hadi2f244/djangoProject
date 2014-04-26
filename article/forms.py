from django import forms
from models import Article
#from django_markdown.widgets import MarkdownWidget
class ArticleForm(forms.ModelForm):
	#content = forms.CharField( widget=MarkdownWidget() )	

	class Meta:
		model=Article
		fields= ('title','body','pub_date')
	
