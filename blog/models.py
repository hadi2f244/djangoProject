from django.db import models
from django.contrib.auth.models import User
#from blog.article.models import Article,Comment
#from blog.category.models import Category
#from user.models import User # in main project
class Blog(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    domain=models.CharField(unique=True,max_length=200)
    #user=models.ForeignKey(User)

    name=models.CharField(max_length=200)
    def __unicode__(self):              # __unicode__ on Python 2
        return self.domain
