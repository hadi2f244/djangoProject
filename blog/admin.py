from django.contrib import admin
from blog.models import Blog
from django.contrib.admin import ModelAdmin
from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _






class BlogChangeForm(forms.ModelForm):

    class Meta:
        model = Blog

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class blogAdmin(ModelAdmin):

    change_form_template = 'admin/blog/extras/blog_changed_template.html'
    form = BlogChangeForm

    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['sitename'] = settings.SITE_NAME
        return super(blogAdmin, self).change_view(request, object_id,
            form_url, extra_context=extra_context)


    fieldsets = (
        (None, {'fields': ('user', 'domain', 'name',)}),
        #('Data', {'fields': ('domain', 'name')}),
    )

    '''
    def get_form(self, request, obj=None, **kwargs):
        #self.exclude = []
        #if not request.user.is_superuser:
        #    self.exclude.append('field_to_hide')
        self.form.BlogAddress = "www.google.com"
        return super(blogAdmin, self).get_form(request, obj, **kwargs)
    '''

admin.site.register(Blog, blogAdmin)


