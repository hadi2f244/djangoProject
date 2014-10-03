from django.db import models
from blog.apps.blog.models import Blog
from django.utils.translation import ugettext_lazy as _

class Category(models.Model):
    title = models.CharField(verbose_name=_('title'),max_length=200)
    blog=models.ForeignKey(Blog,verbose_name=_('blog'))

    def __unicode__(self):
        return self.title
    class Meta:
        app_label = "blog"
        verbose_name=_('Category')
        verbose_name_plural=_('Categories')