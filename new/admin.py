from django.contrib import admin
from new.models import New
from ckeditor.widgets import CKEditorWidget
from django import forms


class NewAdminForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = New


class NewAdmin(admin.ModelAdmin):
    form = NewAdminForm


admin.site.register(New, NewAdmin)



