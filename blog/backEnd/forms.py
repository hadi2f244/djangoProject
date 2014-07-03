from django.contrib.auth.forms import PasswordChangeForm,UserChangeForm
from django import forms
from django.utils.datastructures import SortedDict
from django.utils.translation import ugettext, ugettext_lazy as _

class profileForm(PasswordChangeForm):
    pass
'''    username = forms.RegexField(
        label=_("Username"), max_length=30, regex=r"^[\w.@+-]+$",
        help_text=_("Required. 30 characters or fewer. Letters, digits and "
                      "@/./+/-/_ only."),
        error_messages={
            'invalid': _("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")})
   # email=EmailField()'''
'''def save(self, commit=True):
        self.user.username=self.cleaned_data['username']
        #self.user.email=self.cleaned_data['email']
        self.user.set_password(self.cleaned_data['new_password1'])
        if commit:
            self.user.save()
        return self.user
profileForm.base_fields = SortedDict([
    (k, profileForm.base_fields[k])
    for k in ['username','old_password', 'new_password1', 'new_password2']
])'''