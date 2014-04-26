from django.db import models
import datetime

# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	pub_date = models.DateTimeField('data published',default=datetime.datetime.now)
	likes = models.IntegerField(default = 0)
	
	def __unicode__(self):
		return self.title

class Comment(models.Model):
	writer = models.CharField(max_length = 100)
	body = models.TextField()
	date = models.DateTimeField('commented date',default=datetime.datetime.now)
	article = models.ForeignKey(Article)

	def __unicode__(self):              # __unicode__ on Python 2
		return self.writer

	class Meta:
		ordering = ('date',)


