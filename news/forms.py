from news.models import News
from datetime import datetime
from django import forms
from django_bleach.forms import BleachField
############################################################################################

class NewsForm(forms.ModelForm):
    title = forms.CharField(max_length=200)
    body = BleachField()#widget=CKEditorWidget())
    pub_date = forms.DateTimeField(initial = datetime.now())
    hide = forms.BooleanField(initial= False, required=False)

    class Meta:
        model= News
        fields = ['title','body', 'hide','pub_date']
