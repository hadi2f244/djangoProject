# Create your views here.
from django.http import HttpResponse
#from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
from article.models import Article, Comment
from django.core.context_processors import csrf 
from django.http import HttpResponseRedirect
from forms import ArticleForm
'''
def hello(request):
	name='world'
	t= get_template('hello.html')
	html= t.render(Context({'name':name}))
	return HttpResponse(html)

class helloClass(TemplateView):
	template_name = 'hello.html'
	def get_context_data(self,**kwargs):
		context = super(helloClass,self).get_context_data(**kwargs)
		context['name']='world'
		return context
'''

def articles(request):
	language = "en-gb"
	session_language = "en-gb"
	if 'lang' in request.COOKIES :
		language = request.COOKIES['lang']
	if 'lang' in request.session:
		session_language = request.session['lang']
	
	return render_to_response('articles.html',
							{'articles' : Article.objects.all(),
							 'language' : language, 
							 'session_language' : session_language})

def article(request,article_id=1):
	comments = Comment.objects.filter(article = article_id)#article_id)
	#actors = Actor.objects.filter(programme = programme_id)
	#print comments
	#comments = Comment.objects.filter(article__title = 'khar')	
	return render_to_response('article.html',
							{'article' : Article.objects.get(id=article_id),
							'commnets' : comments })

def language(request,language='en-gb'):
	response = HttpResponse("setting language to %s"% language)
	response.set_cookie('lang',language)
	request.session['lang'] = language
	return response

def create(request):
	if request.POST:
		form = ArticleForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/articles/all")
	else:
		form = ArticleForm()
	args={}
	args.update(csrf(request))
	args['form']=form
	return render_to_response('create_article.html',args)

def like_article(request,article_id):
	if article_id:
		a=Article.objects.get(id=article_id)
		count = a.likes
		count +=1
		a.likes = count
		# i must use csrf for likes,too
		a.save()
	return HttpResponseRedirect('/articles/get/%s'% article_id)
