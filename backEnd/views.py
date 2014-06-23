
from django.shortcuts import render_to_response
from article.models import Article, Comment
from category.models import Category
from article.forms import ArticleForm,CommentForm#,ArticleForm_edit
from django.contrib import auth
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from functools import wraps

def backEnd(view):
    @wraps(view)
    def wrapper(request,*args,**kwargs):
        context= {} #context is data that will be replace with template variable
        context['userAuthenticated']=request.user.is_authenticated() and request.user.is_superuser
        if not context['userAuthenticated']:
            return HttpResponseRedirect("/administrator")
        context['user']=request.user
        return view(request,context,*args,**kwargs)
    return wrapper

################################################################################################
#account login views
def login(request):
    context={}
    userAuthenticated = request.user.is_authenticated() and request.user.is_superuser
    context.update(csrf(request))
    if userAuthenticated : # if the user was activated
        return HttpResponseRedirect('/administrator/dashBoard')

    elif (request.method == "GET"): #if user not loggedin and  the first time that page loaded we create csrf num
        return render_to_response('backEnd/djangoBlog/login.html', context)

    else: # the POST with username and pass came :
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect('/administrator/dashBoard')

        else : #if invalid username and pass entered we recreate a csrf num
            context['invalid']=True
            return render_to_response('backEnd/djangoBlog/login.html',context)

#################################################################################################
@backEnd
def dashBoard(request,context):
    return render_to_response('backEnd/djangoBlog/dashBoard.html',context)

#################################################################################################
@backEnd
def articles(request,context):
    context.update(csrf(request))
    if 'deleteButton' in request.POST: #Delete button clicked!
        checked=request.POST.getlist("articleIdCheckes")
        if not len(checked):
            return HttpResponseRedirect("")
        for articleID in checked:
            Article.objects.get(id=articleID).delete() #we must check the delete process correction ####
    context['articles'] = Article.objects.all()
    return render_to_response("backEnd/article/articles.html",context)

#################################################################################################
@backEnd
def article(request,context,article_id=1):#just show the article
    #if article with this article_id doesn't exist ####
    context.update(csrf(request))
    context['article'] = Article.objects.get(id=article_id)
    context['categories'] = context['article'].category.all()

    return render_to_response("backEnd/article/article.html",context)
#################################################################################################
@backEnd
def articleDel(request,context,article_id=1):
    #if article with this article_id doesn't exist ####
    Article.objects.get(id=article_id).delete() #we must check the delete process correction ####
    # after deletation a box must show that ####
    return HttpResponseRedirect("/administrator/articles/all")
################################################################################################

@backEnd
def articleEdit(request,context,article_id):
    #if article with this article_id doesn't exist ####
    context.update(csrf(request))
    lastArticle=Article.objects.get(id=article_id)
    if lastArticle is None: # Is there any article to edit!
        return HttpResponseRedirect("/administrator/articles/all")

    if 'submitArticle' in request.POST: #make sure that user click save button
        articleForm = ArticleForm(request.POST,instance=lastArticle) #to edit we set instance otherwise this create new article
        if articleForm.is_valid():
            articleForm.save()
            return HttpResponseRedirect("/administrator/articles/get/"+article_id)
    else:# if user enter for first time So needed to show article informations
        articleForm=ArticleForm(instance=lastArticle)
    context['method']='articleEdit'
    context['article_id']=article_id
    context['form']=articleForm
    return render_to_response('backEnd/article/submit_article.html',context)

################################################################################################
'''
@backEnd
def articleCreate(request,context):
    context.update(csrf(request))
    if 'submitArticle' in request.POST: #means you click on submit button named createArticle in create_article.html
        form = ArticleForm(request.POST)
        if form.is_valid():
            title=request.POST['title']
            body=request.POST['body']
            article=Article.objects.create(title=title,body=body)
            # use created article's id to redirect to /get/article.id
            return HttpResponseRedirect("/administrator/articles/get/"+str(article.id))
    else:
        form = ArticleForm()#create a simple ArticleForm

    context['method']='articleCreate'
    context['form']=form
    return render_to_response('backEnd/article/submit_article.html',context)
'''
@backEnd
def articleCreate(request,context):
    context.update(csrf(request))
    if 'submitArticle' in request.POST: #means you click on submit button named createArticle in create_article.html
        form = ArticleForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect("/administrator/articles/get/"+str((form.save()).id))
    else:
        form = ArticleForm()#create a simple ArticleForm
    context['method']='articleCreate'
    context['form']=form
    return render_to_response('backEnd/article/submit_article.html',context)
#################################################################################################
@backEnd
def categories(request,context):
    context.update(csrf(request))
    if 'deleteButton' in request.POST: #Delete button clicked!
        checked=request.POST.getlist("categoryIdCheckes")
        if not len(checked):
            return HttpResponseRedirect("")
        for categoryID in checked:
            Category.objects.get(id=categoryID).delete() #we must check the delete process correction ####
    context['categories'] = Category.objects.all()
    return render_to_response("backEnd/category/categories.html",context)