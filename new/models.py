from django.db import models
import datetime
from ckeditor.fields import RichTextField
from django.utils.translation import ugettext_lazy as _
############################################################################################

# Create your models here.
class New(models.Model):
    title = models.CharField(verbose_name=_('Title'),max_length=200)
    body = RichTextField(verbose_name=_('Body'))
    pub_date = models.DateTimeField(verbose_name=_('Published date'),default=datetime.datetime.now)
    hide = models.BooleanField(verbose_name=_('Hide'))
    class Meta:
        verbose_name = _('New')
    def __unicode__(self):
        return self.title

