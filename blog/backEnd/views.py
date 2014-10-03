from django.shortcuts import render
from blog.apps.article.models import Article
from blog.apps.comment.models import Comment
from blog.apps.category.models import Category
from blog.apps.blog.models import Blog
from blog.apps.article.forms import ArticleForm
from blog.apps.comment.forms import CommentFormEdit
from django.contrib import auth
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from functools import wraps
from blog.backEnd.forms import profileForm
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

def backEnd(view):
    @wraps(view)
    def wrapper(request,*args,**kwargs):
        context= {} #context is data that will be replace with template variable
        context['userAuthenticated']=request.user.is_authenticated() and (request.user==request.blog.user or request.user.is_superuser) #and request.user.is_superuser
        if not context['userAuthenticated']:
            return HttpResponseRedirect("/administrator")
        context['log']="domainName: "+request.blog.domain
        context['user']=request.user
        return view(request,context,*args,**kwargs)
    return wrapper

################################################################################################
#account login views
def login(request):
    context={}
    userAuthenticated = request.user.is_authenticated() and (request.user==request.blog.user or request.user.is_superuser)

    if userAuthenticated : # if the user was activated
        return HttpResponseRedirect('/administrator/dashBoard')

    elif (request.method == "GET"): #if user not loggedin and  the first time that page loaded we create csrf num
        return render(request,'backEnd/djangoBlog/login.html', context)

    else: # the POST with username and pass came :
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        user=auth.authenticate(username=username,password=password)
        if user and (request.blog.user==user or user.is_superuser):
            auth.login(request,user)
            return HttpResponseRedirect('/administrator/dashBoard')

        else : #if invalid username and pass entered we recreate a csrf num
            context['invalid']=True
            return render(request,'backEnd/djangoBlog/login.html',context)

#################################################################################################
def logout(request):
    userAuthenticated = request.user.is_authenticated() and (request.user==request.blog.user or request.user.is_superuser)
    if userAuthenticated:
        auth.logout(request)
    return HttpResponseRedirect("/administrator")
#################################################################################################
@backEnd
def dashBoard(request,context):
    return render(request,'backEnd/djangoBlog/dashBoard.html',context)

#################################################################################################
#################################################################################################
#Articles:

@backEnd
def articles(request,context):

    if 'deleteButton' in request.POST: #Delete button clicked!
        checked=request.POST.getlist("articleIdCheckes")
        if not len(checked):
            return HttpResponseRedirect("")
        for articleID in checked:
            request.blog.article_set.get(id=articleID).delete() #we must check the delete process correction ####
    elif 'HideButton' in request.POST: #Delete button clicked!
        checked=request.POST.getlist("articleIdCheckes")
        if not len(checked):
            return HttpResponseRedirect("")
        for articleID in checked:
            ob = request.blog.article_set.get(id=articleID)
            ob.hide = True
            ob.save()

    context['articles'] = request.blog.article_set.all()
    return render(request,"backEnd/article/articles.html",context)

#################################################################################################
@backEnd
def article(request,context,article_slug):#just show the article
    #if article with this article_id doesn't exist ####
    try:
        context['article'] = request.blog.article_set.get(slug=article_slug)
    except ObjectDoesNotExist:
        raise Http404
    context['categories'] = context['article'].category.all()

    return render(request,"backEnd/article/article.html",context)
#################################################################################################
@backEnd
def articleDel(request,context,article_slug):
    #if article with this article_id doesn't exist ####
    request.blog.article_set.get(slug=article_slug).delete() #we must check the delete process correction ####
    # after deletation a box must show that ####
    return HttpResponseRedirect("/administrator/articles/all")
################################################################################################
####w
@backEnd
def articleEdit(request,context,article_slug):
    #if article with this article_id doesn't exist ####

    lastArticle=request.blog.article_set.get(slug=article_slug)#So we dont need to send blog.id to ArticleForm that did in articleCreate views
    if lastArticle is None: # Is there any article to edit!
        return HttpResponseRedirect("/administrator/articles/all")

    if 'submitArticle' in request.POST: #make sure that user click save button
        articleForm = ArticleForm(request.blog.id,request.POST,instance=lastArticle) #to edit we set instance otherwise this create new article
        if articleForm.is_valid():
            articleForm.save()
            return HttpResponseRedirect("/administrator/articles/get/"+article_slug)
    else:# if user enter for first time So needed to show article informations
        articleForm=ArticleForm(blog_id=request.blog.id,instance=lastArticle)
    context['method']='articleEdit'
    context['article_slug']=article_slug
    context['form']=articleForm
    return render(request,'backEnd/article/submit_article.html',context)

################################################################################################
@backEnd
def articleCreate(request,context):

    if 'submitArticle' in request.POST: #means you click on submit button named createArticle in submit_article.html
        articleForm = ArticleForm(request.blog.id,request.POST)
        if articleForm.is_valid():
            article=articleForm.save(commit=False)
            article.blog_id=request.blog.id
            article.save()
            #print article.body
            return HttpResponseRedirect("/administrator/articles/get/"+str(article.slug))
    else:
        articleForm = ArticleForm(request.blog.id)#create a simple ArticleForm
    context['method']='articleCreate'
    context['form']=articleForm
    return render(request,'backEnd/article/submit_article.html',context)
#################################################################################################
#################################################################################################
#Category:

@backEnd
def categories(request,context):

    if 'deleteButton' in request.POST: #Delete button clicked!
        checked=request.POST.getlist("categoryIdCheckes")
        if not len(checked):
            return HttpResponseRedirect("")
        for categoryID in checked:
            request.blog.category_set.get(id=categoryID).delete() #we must check the delete process correction ####
    context['categories'] = request.blog.category_set.all()
    return render(request,"backEnd/category/categories.html",context)

##################################################################################################
@backEnd
def categoryCreate(request,context):

    if 'submitCategory' in request.POST:#means you click on submit button named createCategory in submit_category.html
        ctg=request.blog.category_set.create(title=request.POST['categoryName'])
        return HttpResponseRedirect("/administrator/categories/get/"+str(ctg.id))
    context['method']='categoryCreate'
    return render(request,'backEnd/category/submit_category.html',context)

##################################################################################################
@backEnd
def category(request,context,category_id):
    context['category']=request.blog.category_set.get(id=category_id)
    context['articles']=request.blog.article_set.filter(category__id=category_id).distinct()
    return render(request,"backEnd/category/category.html",context)
###################################################################################################
@backEnd
def categoryDel(request,context,category_id):
    request.blog.category_set.get(id=category_id).delete() #we must check the delete process correction ####
    return HttpResponseRedirect("/administrator/categories/all")
###################################################################################################
@backEnd
def categoryEdit(request,context,category_id):

    lastCtg=request.blog.category_set.get(id=category_id)
    if lastCtg is None:
        return HttpResponseRedirect("/administrator/categories/all")
    if 'submitCategory' in request.POST: #make sure that user click save button
        lastCtg.title=request.POST['categoryName']
        lastCtg.save()
        return HttpResponseRedirect("/administrator/categories/get/"+category_id)

    context['method']='categoryEdit'
    context['category_id']=category_id
    context['category_title']=lastCtg.title
    return render(request,'backEnd/category/submit_category.html',context)

#################################################################################################
#################################################################################################
#Comment:

@backEnd
def comments(request,context): #we want to show to all of comments ordering to date_created

    if 'deleteButton' in request.POST: #Delete button clicked!
        checked=request.POST.getlist("commentIdCheckes")
        if not len(checked):
            return HttpResponseRedirect("")
        for commentID in checked:
            request.blog.comment_set.get(id=commentID).delete() #we must check the delete process correction ####


    comments=request.blog.comment_set.all()
    com_art=[] # commment & article together
    for comment in comments:
        com_art.append((comment,request.blog.article_set.get(id=comment.article_id)))
    context['com_art']=com_art
    return render(request,'backEnd/comment/comments.html',context)
#must create a field named seen in comment model(default=False) that shows that admin saw that. migrate the comments

###################################################################################################
@backEnd
def cArticles(request,context):
    articles=request.blog.article_set.all()
    art_lComs=[]#article and length of comment set together
    for article in articles:
        art_lComs.append((article,len(request.blog.comment_set.filter(article=article))))
    context['art_lComs']=art_lComs
    return render(request,"backEnd/comment/cArticles.html",context)
###################################################################################################

@backEnd
def cArticle(request,context,article_slug):
    context['article'] = request.blog.article_set.get(slug=article_slug)
    context['commnets'] = request.blog.comment_set.filter(article = context['article'].id)
    for cmt in context['commnets']:
        cmt.seen=True
        cmt.save()
    return render(request,'backEnd/comment/cArticle.html',context)

###################################################################################################
#coment: #### create a see method for comments
@backEnd
def comment(request,context,comment_id):#we show the comment details
    context['comment']=request.blog.comment_set.get(id=comment_id)
    context['articleName']=request.blog.article_set.get(id=context['comment'].article_id).title
    return render(request,"backEnd/comment/comment.html",context)

###################################################################################################
@backEnd
def commentDel(request,context,comment_id):
    request.blog.comment_set.get(id=comment_id).delete()#we must check the delete process correction ####
    return  HttpResponseRedirect("/administrator/comments/all")
###################################################################################################
@backEnd
def commentEdit(request,context,comment_id):

    lastCmt=request.blog.comment_set.get(id=comment_id)
    if lastCmt is None:
        return HttpResponseRedirect("/administrator/comments/all")
    if 'submitComment' in request.POST: #make sure that user click save button
        cmtForm=CommentFormEdit(request.POST,instance=lastCmt)
        if cmtForm.is_valid():
            cmtForm.save()
            return HttpResponseRedirect("/administrator/comments/get/"+comment_id)
    else:
        cmtForm=CommentFormEdit(instance=lastCmt)


    context['method']='commentEdpiit'
    context['comment_id']=comment_id
    context['form']=cmtForm
    return render(request,'backEnd/comment/submit_comment.html',context)
###################################################################################################
###################################################################################################
#profile views:

@backEnd
def profile(request,context):

    #we show NickName,username,email and work with oldPass & newPass & confirm newPass
    passForm=profileForm(user=request.user) #that was defined in django.contrib.auth.forms .It recieves the user to check old pass
    if 'submitButton' in request.POST:
        passForm=profileForm(user=request.user,data=request.POST)
        if passForm.is_valid():
            passForm.save()
            context['notifications']= "Your password was changed , successfully!"#is in the base
            context['passForm']=passForm
            return render(request,'backEnd/profile/profile.html',context)
   # else:
       # context['passForm']=profileForm(user=request.user)
    context['passForm']=passForm
    return render(request,'backEnd/profile/profile.html',context)