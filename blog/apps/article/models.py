from django.db import models
import datetime
from django.core.urlresolvers import reverse
from blog.apps.category.models import Category
from blog.apps.blog.models import Blog
from django_bleach.models import BleachField
from django.utils.translation import ugettext_lazy as _
import jdatetime
from django_jalali.db import models as jmodels
############################################################################################

# Create your models here.
class Article(models.Model):
    #objects = jmodels.jManager()
    title = models.CharField(verbose_name=_('title'),max_length=200)
    slug = models.SlugField(verbose_name=_('slug'),max_length=50,unique=True)
    body = BleachField(verbose_name=_('Body'))
    pub_date = jmodels.jDateField(default=jdatetime.date.today())#models.DateTimeField(verbose_name=_('Published date'),default=datetime.datetime.now)
    #likes = models.IntegerField(default = 0)
    hide = models.BooleanField(verbose_name=_('hide'))
    category = models.ManyToManyField(Category,verbose_name=_('Category'),blank=True)
    blog=models.ForeignKey(Blog,verbose_name=_('blog'))

    def __unicode__(self):
        return self.title

    def get_category(self):
        return self.category

    @models.permalink
    def get_absolute_url(self):
        return ('views.view_something', (), {'slug': self.slug})
    class Meta:
        app_label = "blog"
        verbose_name=_('Article')
        verbose_name_plural=_('Articles')

