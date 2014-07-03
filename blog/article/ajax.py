from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from blog.article.models import Article

    
@dajaxice_register
def likeJax(request, data1):
    if data1:
		article=Article.objects.get(id=data1)
		count = article.likes
		count +=1
		article.likes = count
		# i must use csrf for likes,too
		article.save()
    
    
    return simplejson.dumps({'message':'Hello from Python!', 'likes_num':article.likes})
