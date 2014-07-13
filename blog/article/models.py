from django.db import models
import datetime
import tinymce.models as tinymce
from django.core.urlresolvers import reverse
from blog.category.models import Category
from blog.models import Blog
############################################################################################

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('data published',default=datetime.datetime.now)
    likes = models.IntegerField(default = 0)
    hide = models.BooleanField()
    category = models.ManyToManyField(Category,blank=True)
    blog=models.ForeignKey(Blog)

    def __unicode__(self):
        return self.title

    def get_category(self):
        return self.category

    def get_absolute_url(self):
        return reverse('article.views.article', args=[str(self.id)])


############################################################################################

class Comment(models.Model):
    writer = models.CharField(max_length = 100)
    body = models.TextField()
    date = models.DateTimeField('commented date',default=datetime.datetime.now)
    article = models.ForeignKey(Article)
    seen = models.BooleanField(default=False)
    blog=models.ForeignKey(Blog)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.writer

    class Meta:
        ordering = ('date',)


