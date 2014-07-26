from django.db import models
from user.models import MyUser # in main project
from django.utils.translation import ugettext_lazy as _

class Blog(models.Model):
    user = models.OneToOneField(MyUser,verbose_name=_('user'), primary_key=True)
    domain=models.CharField(unique=True,verbose_name=_('domain'),max_length=200)
    name=models.CharField(verbose_name=_('name'),max_length=200)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.domain
    class Meta:
        verbose_name=_('Blog')
        verbose_name_plural=_('Blogs')