from django import forms
from django.utils.translation import ugettext_lazy as _

from blog.apps.article.models import Article
from blog.apps.category.models import Category

from django_jalali.forms import DateTimeWidget
############################################################################################

class ArticleForm(forms.ModelForm):
    #title = forms.CharField(max_length=200)
    #body = BleachField()#widget=CKEditorWidget())
    pub_date = forms.DateField(widget=DateTimeWidget)
   # hide = forms.BooleanField(initial= False, required=False)
    category = forms.ModelMultipleChoiceField(label=_("Category"),queryset=Category.objects.all(),widget=forms.CheckboxSelectMultiple,required=False)

    class Meta:
        model= Article
        fields = ['title','body','slug','hide','pub_date','category' ]
        #exclude=['blog']

    def __init__(self,blog_id=None, *args, **kwargs):
        #we overrided the initializing to set category fields choices according to the blog
        super(ArticleForm, self).__init__(*args, **kwargs)

        if blog_id:
            self.fields['category'] = forms.ModelMultipleChoiceField(label=_("Category"),queryset=Category.objects.filter(blog_id=blog_id),widget=forms.CheckboxSelectMultiple,required=False)
            #self.fields['blog_id']=blog,id


        #for key, in self.initial_fields:
         #   if hasattr(self.person, key):
          #      self.fields[k].initial = getattr(self.person, key)


   # def save(self,lastArticle,list):


