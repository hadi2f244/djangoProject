from django.http import HttpResponse
from django.shortcuts import render
from blog.article.models import Article, Comment
from django.core.context_processors import csrf 
from django.http import HttpResponseRedirect
from forms import CommentForm
from blog.views import frontEnd # frontEnd is frontEnd decorator!
##################################################################################################################
@frontEnd
def articles(request,context):
    language = "en-gb"
    session_language = "en-gb"
    if 'lang' in request.COOKIES :
        language = request.COOKIES['lang']
    if 'lang' in request.session:
        session_language = request.session['lang']
    context['articles'] = Article.objects.filter(blog_id=request.blog.id)
    #context['articles'] = Article.objects.get(hide=True)
    context['language'] = language
    context['session_language'] = session_language
    return render(request,'blog/frontEnd/article/articles.html',context)

##################################################################################################################

@frontEnd
def article(request,context,article_id):

    context['article'] = Article.objects.get(id=article_id,blog_id=request.blog.id)
    context['commnets'] = Comment.objects.filter(article = article_id,blog_id=request.blog.id)#article_id)
    if True :#context['userAuthenticated']:#see frontEnd decorator
        #################################
        #check commment create:
        if 'commentButton' in request.POST: #comment(create) button clicked!
            comment_form = CommentForm(request.POST) #if is valid --> save if not we create a new CommentForm with some error for user(like empty field and ...)
            if comment_form.is_valid():
                writer=request.POST['writer']
                body=request.POST['body']
                Comment.objects.create(writer=writer,body=body,article=context['article'],blog_id=request.blog.id)
                return HttpResponseRedirect('') #just for reload the page and cleaning the fields
        else:
            comment_form=CommentForm() #create a simple CommentForm
            ##################################
    else :
        comment_form=None
    #set template variable:
    context['comment_form']=comment_form
    return render(request,'blog/frontEnd/article/article.html',context)

##################################################################################################################

def language(request,language='en-gb'):
	response = HttpResponse("setting language to %s"% language)
	response.set_cookie('lang',language)
	request.session['lang'] = language
	return response


##################################################################################################################


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

