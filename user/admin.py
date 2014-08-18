from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from user.models import MyUser
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from blog.models import Blog
from django.core.exceptions import ObjectDoesNotExist

class UserCreationForm(forms.ModelForm):
    """A form for creating new user. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('username', 'email')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating user. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField(label=_('password'))

    class Meta:
        model = MyUser
        fields = ('username', 'password', 'email', 'is_active', 'is_admin', 'aboutme', 'activation_key')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class MyUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm
    change_form_template = 'admin/user/extras/user_changed_template.html'

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'email', 'is_admin', 'is_active', 'aboutme', 'activation_key')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('email', 'aboutme', 'activation_key')}),
        (_('Permissions'), {'fields': ('is_admin', 'is_active')}),
        #(_('External Links'), {'fields' : ()}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email', 'username')
    ordering = ('email', 'username')
    filter_horizontal = ()
    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        user = MyUser.objects.get(id = object_id)
        try:
            blog = Blog.objects.get(user=user)
            extra_context['blogId'] = blog.id
        except ObjectDoesNotExist:
            extra_context['blogId'] = None

        extra_context['siteName'] = settings.SITE_NAME
        return super(MyUserAdmin, self).change_view(request, object_id,
            form_url, extra_context=extra_context)

# Now register the new UserAdmin...
admin.site.register(MyUser, MyUserAdmin)
# ... and, since we're not using Django's builtin permissions,
# unregister the Group model from admin.
admin.site.unregister(Group)


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
'''class MyUserInline(admin.StackedInline):
    model = MyUser
    can_delete = False
    verbose_name_plural = 'myuser'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (MyUserInline, )




admin.site.unregister(User)
admin.site.register(User, UserAdmin)
'''