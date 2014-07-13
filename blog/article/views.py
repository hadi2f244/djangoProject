# Create your views here.
from django.http import HttpResponse
#from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from blog.article.models import Article, Comment
from django.core.context_processors import csrf 
from django.http import HttpResponseRedirect
from forms import ArticleForm,CommentForm#,ArticleForm_edit
from blog.views import frontEnd # frontEnd is frontEnd decorator!
##################################################################################
'''
class frontEnd1(TemplateView):
	#template_name =
	def get_context_data(self, **kwargs):
		context = super(frontEnd1, self).get_context_data(**kwargs)
		context['userAuthenticated']=self.request.user.is_authenticated
		context['user']=self.request.user
		return context
'''

##################################################################################################################
'''
class articles(frontEnd1):
	template_name='articles.html'
	def get(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		language = "en-gb"
		session_language = "en-gb"
		if 'lang' in request.COOKIES :
			language = request.COOKIES['lang']
		if 'lang' in request.session:
			session_language = request.session['lang']
		context['articles'] = Article.objects.all()
		context['language'] = language
		context['session_language'] = session_language
		return self.render_to_response(context)
'''
@frontEnd
def articles(request,context):
    language = "en-gb"
    session_language = "en-gb"
    if 'lang' in request.COOKIES :
        language = request.COOKIES['lang']
    if 'lang' in request.session:
        session_language = request.session['lang']
    context['articles'] = Article.objects.filter(blog_id=request.blog.user_id)
    #context['articles'] = Article.objects.get(hide=True)
    context['language'] = language
    context['session_language'] = session_language
    return render_to_response('blog/frontEnd/article/articles.html',context)

##################################################################################################################
'''
class article(frontEnd1):
	template_name="article.html"
	def get(self,request,*args,**kwargs):
		context = self.get_context_data(**kwargs)
		article_id=self.kwargs['article_id']


		context.update(csrf(request))
		article = Article.objects.get(id=article_id)
		comments = Comment.objects.filter(article = article_id)
		if request.user.is_authenticated():
			comment_form=CommentForm()
		else:-

			comment_form=None

		#set template variable:
		context['comment_form']=comment_form
		context['article'] =article
		context['commnets'] = comments
		return self.render_to_response(context)

	def post(self,request,*args,**kwargs):
		context = self.get_context_data(**kwargs)
		article_id=self.kwargs['article_id']
		
		context.update(csrf(request))
		article = Article.objects.get(id=article_id)
		comments = Comment.objects.filter(article = article_id)
		if request.user.is_authenticated():
		
		#################################
		#check commment create:
			if 'commentButton' in request.POST: #comment(create) button clicked!
				comment_form =CommentForm(request.POST) #if is valid --> save if not we create a new CommentForm with some error for user(like empty field and ...)
				if comment_form.is_valid():
					writer=request.POST['writer']
					body=request.POST['body']
					Comment.objects.create(writer=writer,body=body,article=article)
					comment = Comment.objects.create(writer=writer,body=body,article=article)
					return HttpResponseRedirect('') #just for reload the page and cleaning the fields
			else:
				comment_form=CommentForm() #create a simple CommentForm
		##################################
		else :
			comment_form=None
		#set template variable:
		context['comment_form']=comment_form
		context['article'] =article
		context['commnets'] = comments
		return self.render_to_response(context)
'''		

@frontEnd
def article(request,context,article_id):
    context.update(csrf(request))
    context['article'] = Article.objects.get(id=article_id,blog_id=request.blog.user_id)
    context['commnets'] = Comment.objects.filter(article = article_id,blog_id=request.blog.user_id)#article_id)
    if True :#context['userAuthenticated']:#see frontEnd decorator
        #################################
        #check commment create:
        if 'commentButton' in request.POST: #comment(create) button clicked!
            comment_form = CommentForm(request.POST) #if is valid --> save if not we create a new CommentForm with some error for user(like empty field and ...)
            if comment_form.is_valid():
                writer=context['user'] #see frontEnd decorator
                body=request.POST['body']
                Comment.objects.create(writer=writer,body=body,article=context['article'],blog_id=request.blog.user_id)
                #comment = Comment.objects.create(writer=writer,body=body,article=article)
                return HttpResponseRedirect('') #just for reload the page and cleaning the fields
        else:
            comment_form=CommentForm() #create a simple CommentForm
            ##################################
    else :
        comment_form=None
    #set template variable:
    context['comment_form']=comment_form
    return render_to_response('blog/frontEnd/article/article.html',context)

##################################################################################################################

def language(request,language='en-gb'):
	response = HttpResponse("setting language to %s"% language)
	response.set_cookie('lang',language)
	request.session['lang'] = language
	return response

##################################################################################################################
'''
class create_article(frontEnd1):
	template_name="submit_article.html"

	def get(self,request,*args,**kwargs):
		context = self.get_context_data(**kwargs)
		context.update(csrf(request))
		form = ArticleForm()#create a simple ArticleForm
		context['form']=form
		return self.render_to_response(context)

	def post(self,request,*args,**kwargs):
		context = self.get_context_data(**kwargs)

		context.update(csrf(request))
		if 'submitArticle' in request.POST: #means you click on submit button named createArticle in create_article.html 
			form = ArticleForm(request.POST)
			if form.is_valid():
				title=request.POST['title']
				body=request.POST['body']
				Article.objects.create(title=title,body=body)
				return HttpResponseRedirect("/articles/all")
		else:
			form = ArticleForm()#create a simple ArticleForm
		context['form']=form
		return self.render_to_response(context)

'''

##################################################################################################################
'''
class edit_article(frontEnd1):
	template_name="submit_article.html"
	def get(self,request,*args,**kwargs):
		context = self.get_context_data(**kwargs)
		article_id=self.kwargs['article_id']

		if article_id is None: # Is there any article to edit!
			return HttpResponseRedirect("/articles/all")

		lastArticle=Article.objects.get(id=article_id)
		articleForm=ArticleForm_edit(initial={'title':lastArticle.title,'body':lastArticle.body,'pub_date':lastArticle.pub_date})

		context.update(csrf(request))
		context['form']=articleForm
		return self.render_to_response(context)

	def post(self,request,*args,**kwargs):
		context = self.get_context_data(**kwargs)
		article_id=self.kwargs['article_id']

		if article_id is None: # Is there any article to edit!
			return HttpResponseRedirect("/articles/all")
		
	
		if 'submitArticle' in request.POST: #make sure that user click save button
			articleForm = ArticleForm_edit(request.POST) 
			if articleForm.is_valid():
				lastArticle=Article.objects.get(id=article_id) 
				lastArticle.title = request.POST['title']
				lastArticle.body = request.POST['body']
				lastArticle.pub_date = request.POST['pub_date']
				lastArticle.save()

				return HttpResponseRedirect("/articles/get/"+article_id)	
		else:# if user enter for first time So needed to show article informations
			lastArticle=Article.objects.get(id=article_id)
			articleForm=ArticleForm_edit(initial={'title':lastArticle.title,'body':lastArticle.body,'pub_date':lastArticle.pub_date})


		context.update(csrf(request))
		context['form']=articleForm
		return self.render_to_response(context)

'''


'''
def create_comment(request,article_id):#this function doesn't use like normal view func but this is used near article func
	comment_form =CommentForm(request.POST)
	writer=comment_form.cleaned_data['writer']
	body=comment_form.cleaned_data['body']
	#writer = "Anonymous"
	#if req["writer"]:
	#	writer = req["writer"]
	#r=req
	#req=r.copy() #because querydict is immutable!
	#req.__setitem__('article',str(article_id))
	print req
	if comment_form.is_valid():
		article = Article.objects.get(id=article_id)
		comment = Comment.objects.create(writer=writer,body=body,article=article)
'''
		
	


'''
 p = request.POST

    if p.has_key("body") and p["body"]:
        author = "Anonymous"
        if p["author"]: author = p["author"]

        comment = Comment(post=Post.objects.get(pk=pk))
        cf = CommentForm(p, instance=comment)


        cf.fields["author"].required = False 

        comment = cf.save(commit=False)
        comment.author = author
        comment.save()
    return HttpResponseRedirect(reverse("dbe.blog.views.post", args=[pk]))
'''


'''def like_article(request,article_id):
	if article_id:
		article=Article.objects.get(id=article_id)
		count = article.likes
		count +=1
		article.likes = count
		# i must use csrf for likes,too
		article.save()
	return HttpResponseRedirect('/articles/get/%s'% article_id)
'''

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
