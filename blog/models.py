from django.db import models
#from blog.article.models import Article,Comment
#from blog.category.models import Category
#from user.models import User # in main project
class Blog(models.Model):
    domain=models.CharField(unique=True,max_length=200)
    #user=models.ForeignKey(User)
    name=models.CharField(max_length=200)
