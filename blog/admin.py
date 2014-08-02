from django.contrib import admin
from blog.models import Blog
from django.contrib.admin import ModelAdmin
from django import forms





class BlogChangeForm(forms.ModelForm):
    #test=forms.CharField(max_length=200)
    class Meta:
        model = Blog

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class blogAdmin(ModelAdmin):
    form = BlogChangeForm
    fieldsets = (
        (None, {'fields': ('user','domain','name')}),
        #('Data', {'fields': ('domain', 'name')}),
    )


admin.site.register(Blog,blogAdmin)


