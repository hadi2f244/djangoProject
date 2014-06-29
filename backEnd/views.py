
from django.shortcuts import render_to_response
from article.models import Article, Comment
from category.models import Category
from article.forms import ArticleForm,CommentForm,CommentFormEdit #,ArticleForm_edit
from django.contrib import auth
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from functools import wraps
#from django.contrib.auth.forms import PasswordChangeForm
from backEnd.forms import  profileForm

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
def logout(request):
    userAuthenticated = request.user.is_authenticated() and request.user.is_superuser
    if userAuthenticated:
        auth.logout(request)
    return HttpResponseRedirect("/administrator")
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
def article(request,context,article_id):#just show the article
    #if article with this article_id doesn't exist ####
    #context.update(csrf(request))
    context['article'] = Article.objects.get(id=article_id)
    context['categories'] = context['article'].category.all()

    return render_to_response("backEnd/article/article.html",context)
#################################################################################################
@backEnd
def articleDel(request,context,article_id):
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
    if 'submitArticle' in request.POST: #means you click on submit button named createArticle in submit_article.html
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

##################################################################################################
@backEnd
def categoryCreate(request,context):
    context.update(csrf(request))
    if 'submitCategory' in request.POST:#means you click on submit button named createCategory in submit_category.html
        ctg=Category.objects.create(title=request.POST['categoryName'])
        return HttpResponseRedirect("/administrator/categories/get/"+str(ctg.id))
    context['method']='categoryCreate'
    return render_to_response('backEnd/category/submit_category.html',context)
##################################################################################################

@backEnd
def category(request,context,category_id):
    context['category']=Category.objects.get(id=category_id)
    context['articles']=Article.objects.filter(category__id=category_id).distinct()
    return render_to_response("backEnd/category/category.html",context)
###################################################################################################
@backEnd
def categoryDel(request,context,category_id):
    Category.objects.get(id=category_id).delete() #we must check the delete process correction ####
    return HttpResponseRedirect("/administrator/categories/all")
###################################################################################################
@backEnd
def categoryEdit(request,context,category_id):
    context.update(csrf(request))
    lastCtg=Category.objects.get(id=category_id)
    if lastCtg is None:
        return HttpResponseRedirect("/administrator/categories/all")
    if 'submitCategory' in request.POST: #make sure that user click save button
        lastCtg.title=request.POST['categoryName']
        lastCtg.save()
        return HttpResponseRedirect("/administrator/categories/get/"+category_id)

    context['method']='categoryEdit'
    context['category_id']=category_id
    context['category_title']=lastCtg.title
    return render_to_response('backEnd/category/submit_category.html',context)

###################################################################################################

@backEnd
def comments(request,context): #we want to show to all of comments ordering to date_created
    context.update(csrf(request))
    if 'deleteButton' in request.POST: #Delete button clicked!
        checked=request.POST.getlist("commentIdCheckes")
        if not len(checked):
            return HttpResponseRedirect("")
        for commentID in checked:
            Comment.objects.get(id=commentID).delete() #we must check the delete process correction ####


    comments=Comment.objects.all()
    com_art=[] # commment & article together
    for comment in comments:
        com_art.append((comment,Article.objects.get(id=comment.article_id)))
    context['com_art']=com_art
    return render_to_response('backEnd/comment/comments.html',context)
#must create a field named seen in comment model(default=False) that shows that admin saw that. migrate the comments

###################################################################################################
@backEnd
def cArticles(request,context):
    articles=Article.objects.all()
    art_lComs=[]#article and length of comment set together
    for article in articles:
        art_lComs.append((article,len(article.comment_set.all())))
    context['art_lComs']=art_lComs
    return render_to_response("backEnd/comment/cArticles.html",context)
###################################################################################################

@backEnd
def cArticle(request,context,article_id):
    context['article'] = Article.objects.get(id=article_id)
    context['commnets'] = Comment.objects.filter(article = article_id)#article_id)
    for cmt in context['commnets']:
        cmt.seen=True
        cmt.save()
    return render_to_response('backEnd/comment/cArticle.html',context)

###################################################################################################
#coment: #### create a see method for comments
@backEnd
def comment(request,context,comment_id):#we show the comment details
    context['comment']=Comment.objects.get(id=comment_id)
    context['articleName']=Article.objects.get(id=context['comment'].article_id).title
    return render_to_response("backEnd/comment/comment.html",context)

###################################################################################################
@backEnd
def commentDel(request,context,comment_id):
    Comment.objects.get(id=comment_id).delete()#we must check the delete process correction ####
    return  HttpResponseRedirect("/administrator/comments/all")
###################################################################################################
@backEnd
def commentEdit(request,context,comment_id):
    context.update(csrf(request))
    lastCmt=Comment.objects.get(id=comment_id)
    if lastCmt is None:
        return HttpResponseRedirect("/administrator/comments/all")
    if 'submitComment' in request.POST: #make sure that user click save button
        cmtForm=CommentFormEdit(request.POST,instance=lastCmt)
        if cmtForm.is_valid():
            cmtForm.save()
            return HttpResponseRedirect("/administrator/comments/get/"+comment_id)
    else:
        cmtForm=CommentFormEdit(instance=lastCmt)


    context['method']='commentEdit'
    context['comment_id']=comment_id
    context['form']=cmtForm
    return render_to_response('backEnd/comment/submit_comment.html',context)
###################################################################################################
@backEnd
def profile(request,context):
    context.update(csrf(request))
    #we show NickName,username,email and work with oldPass & newPass & confirm newPass
    passForm=profileForm(user=request.user) #that was defined in django.contrib.auth.forms .It recieves the user to check old pass
    if 'submitButton' in request.POST:
        passForm=profileForm(user=request.user,data=request.POST)
        if passForm.is_valid():
            passForm.save()
            context['notifications']= "Your password was changed , successfully!"#is in the base
            context['passForm']=passForm
            return render_to_response('backEnd/profile/profile.html',context)
   # else:
       # context['passForm']=profileForm(user=request.user)
    context['passForm']=passForm
    return render_to_response('backEnd/profile/profile.html',context)