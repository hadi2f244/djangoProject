from django.db import models
from blog.models import Blog

class Category(models.Model):
    title = models.CharField(max_length=200)
    blog=models.ForeignKey(Blog)

    def __unicode__(self):
        return self.title