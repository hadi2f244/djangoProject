
from django.db import models
import datetime
from blog.apps.article.models import Article
from blog.apps.blog.models import Blog
from django.utils.translation import ugettext_lazy as _
import jdatetime
from django_jalali.db import models as jmodels

class Comment(models.Model):
    writer = models.CharField(verbose_name=_('writer'),max_length = 100)
    body = models.TextField(verbose_name=_('body'))
    date = models.DateTimeField(verbose_name=_('date'),default=datetime.datetime.now)
    article = models.ForeignKey(Article,verbose_name=_('Article'))
    seen = models.BooleanField(verbose_name=_('seen'),default=False)
    blog=models.ForeignKey(Blog,verbose_name=_('blog'))

    def __unicode__(self):              # __unicode__ on Python 2
        return self.writer

    class Meta:
        app_label = "blog"
        verbose_name=_('Comment')
        verbose_name_plural=_('Comments')
        ordering = ('date',)


