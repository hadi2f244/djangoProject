from user.forms import UserCreationForm, RegBlog, loginForm, resetForm, reset_password_form
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from blog.models import Blog
from user.models import MyUser, reset_pass_user
from mainProject.views import frontEnd
from django.template.loader import render_to_string
import random, hashlib
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist




@frontEnd
def register(request,context):
    '''signing up'''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        form1 = RegBlog(request.POST)
        if form.is_valid() and form1.is_valid():
            new_user = form.save()
            username = form.cleaned_data["username"]
            myuser = MyUser.objects.get(username = username)
            myuser.is_active = False
            myuser.save()
            test = form1.cleaned_data
            myblog = Blog.objects.create(user = myuser , domain = test["domain"] , name = test["name"])
            myblog.save()
            #send_user_mail(myuser)
            return render(request,'main/frontEnd/user/registration_complete.html',context)
    else:
        context['form'] = UserCreationForm()
        context['form1'] = RegBlog()
    return render(request, "main/frontEnd/user/registration_form.html",context)

@frontEnd
def activition_complete(request,context, uidb36, token):
    '''compeleting your registration'''
    myuser = MyUser.objects.get(username = token)
    if myuser.activation_key == uidb36 :
        myuser.is_active = True
        myuser.save()
        return render(request, "main/frontEnd/user/activation_complete.html",context)
    else :
        return HttpResponse("information is invalid please register correctlly")

@frontEnd
def set_new_password(request, context, key, email):
    '''
    after sending email which contains a url that route you to this function in order to
    change password
    '''
    if request.method == 'POST':
        form = reset_password_form(request.POST)
        if form.is_valid():
            try:
                simple_user = reset_pass_user.objects.get(email=email, reset_key=key)
                big_user = MyUser.objects.get(email=email)
                big_user.password = form.cleaned_data["password1"]
                big_user.save()
                simple_user.delete()
                return render(request, "main/frontEnd/user/password_reset_complete.html")
            except ObjectDoesNotExist:
                HttpResponse("sql injection")

            '''
            simple_user = reset_pass_user.objects.get(email=email, reset_key=key)
            big_user = MyUser.objects.get(email=email)
            big_user.password = form.cleaned_data["password1"]
            big_user.save()
            simple_user.delete()
            return render(request, "main/frontEnd/user/password_reset_complete.html")
            '''
    context['form'] = reset_password_form()
    return render(request, "main/frontEnd/user/password_change_form.html", context)


@frontEnd
def reset_password(request, context):
    '''
    simple form that you enter your email in it and it will send you an email
    '''

    if request.method == 'POST':
        form = resetForm(request.POST)
        if form.is_valid():
            key = gen()
            email = form.cleaned_data["email"]
            reset_pass_user.objects.create(email=email, reset_key=key)
            send_reset_password_email(email, key)
            return render(request, "main/frontEnd/user/password_reset_email.html", context)
    context['form'] = resetForm()
    return render(request, "main/frontEnd/user/password_reset_form.html", context)


def login(request):
    form = loginForm()
    return render(request, "main/frontEnd/user/login.html", {'form':form})

def send_reset_password_email(email, key):
    '''sending email to users'''
    send_mail('reset_email', 'http://test1.com:8000/accounts/'+key+'-'+email+'/setpassword/', 'sarsanaee@gmail.com',
        [email], fail_silently=False)


def send_user_mail(user):
    '''sending activation email to users'''
    ctx_dict = {'activation_key': user.activation_key,
                    'expiration_days': 7,#settings.ACCOUNT_ACTIVATION_DAYS,
                    'site': "mysite.com",
                    'username': user.username }

    subject = render_to_string('main/frontEnd/user/activation_email_subject.txt',
                                   ctx_dict)
    # Email subject *must not* contain newlines
    subject = ''.join(subject.splitlines())

    message = render_to_string('main/frontEnd/user/activation_email.txt',
                            ctx_dict)

    #ser.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)
    send_mail(subject, message, 'sarsanaee@gmail.com',
        [user.email], fail_silently=False)

def gen():
    salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
    return hashlib.sha1(salt).hexdigest()