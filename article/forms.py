from django.forms import ModelForm
from models import Article,Comment
from tinymce.widgets import TinyMCE
from category.models import Category
from django import forms

############################################################################################

class ArticleForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(),widget=forms.CheckboxSelectMultiple,required=False)
    class Meta:
        model= Article
        fields=['title','body','pub_date','category']
   # def save(self,lastArticle,list):
###########################################################################################
class CommentFormEdit(forms.ModelForm):
    class Meta:
        model=Comment


'''
class ArticleForm(forms.Form): # it must convert to forms.Form for better speed
    #content = forms.CharField( widget=MarkdownWidget() )
    title = forms.CharField(max_length=200)
    body = forms.CharField(widget=TinyMCE(attrs={'cols': 70, 'rows': 20}))
'''
############################################################################################
'''
class ArticleForm_edit(forms.Form):
    title = forms.CharField(max_length=200)
    body = forms.CharField(widget=TinyMCE())#attrs={'cols': 70, 'rows': 20}
    pub_date = forms.DateTimeField()
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(),widget=forms.CheckboxSelectMultiple,required=False)
'''

############################################################################################

class CommentForm(forms.Form):
    #body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    #writer = forms.CharField(max_length = 100)
    body = forms.CharField(widget=forms.Textarea)
