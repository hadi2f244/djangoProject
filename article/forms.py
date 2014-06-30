from django.forms import ModelForm
from models import Article,Comment
from tinymce.widgets import TinyMCE
from category.models import Category
from datetime import datetime
from django import forms
from ckeditor.widgets import CKEditorWidget


############################################################################################

class ArticleForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(),widget=forms.CheckboxSelectMultiple,required=False)
    title = forms.CharField(max_length=200)
    body = forms.CharField(widget=CKEditorWidget())
    pub_date = forms.DateTimeField(initial = datetime.now())
    hide = forms.BooleanField(initial= False, required=False)


    class Meta:
        model= Article
        fields = ['category','title','body', 'hide' ]


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
