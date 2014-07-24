from django.db import models
import datetime
from ckeditor.fields import RichTextField
############################################################################################

# Create your models here.
class New(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextField()
    pub_date = models.DateTimeField('data published',default=datetime.datetime.now)
    hide = models.BooleanField()

    def __unicode__(self):
        return self.title
