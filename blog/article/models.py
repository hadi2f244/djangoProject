from django.db import models
import datetime
from django.core.urlresolvers import reverse
from blog.category.models import Category
from blog.models import Blog
from django.utils.translation import ugettext_lazy as _
############################################################################################

# Create your models here.
class Article(models.Model):
    title = models.CharField(verbose_name=_('title'),max_length=200)
    body = models.TextField(verbose_name=_('body'))
    pub_date = models.DateTimeField(verbose_name=_('Published date'),default=datetime.datetime.now)
    #likes = models.IntegerField(default = 0)
    hide = models.BooleanField(verbose_name=_('hide'))
    category = models.ManyToManyField(Category,verbose_name=_('Category'),blank=True)
    blog=models.ForeignKey(Blog,verbose_name=_('blog'))

    def __unicode__(self):
        return self.title

    def get_category(self):
        return self.category

    def get_absolute_url(self):
        return reverse('article.views.article', args=[str(self.id)])
    class Meta:
        verbose_name=_('Article')
        verbose_name_plural=_('Articles')

############################################################################################

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
        verbose_name=_('Comment')
        verbose_name_plural=_('Comments')
        ordering = ('date',)


