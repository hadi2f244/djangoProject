from django.db import models
import hashlib
import random
from django.template.loader import render_to_string
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

from django.contrib.auth.models import User
import datetime

class MyUserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email :
            raise ValueError('Users must have an email address')

        if not username :
            raise ValueError("Users must have an username address")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(username,
            email=email,
            password=password,

        )
        user.is_admin = True
        user.save(using=self._db)
        return user

def gen():
    salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
    return hashlib.sha1(salt).hexdigest()

class MyUser(AbstractBaseUser):

    username = models.CharField(
        verbose_name="Username",
        max_length=255,
        unique=True,
    )


    email = models.EmailField(
        verbose_name='Email Address',
        max_length=255,
    )

    aboutme = models.CharField(
        verbose_name="about me",
        max_length=255,
    )

    activation_key = models.CharField(
        verbose_name= 'activation key',
        max_length=40,
        #default = self.activation_key_generator()
        default= gen()
    )


    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']#'aboutme', 'activation_key']

    def get_full_name(self):
        # The user is identified by their email address
        return self.username

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def __str__(self):              # __unicode__ on Python 2
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_superuser(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


#correct
#######################################################################################################################

'''
def gen():
    salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
    return hashlib.sha1(salt).hexdigest()


class MyUser(User):
    aboutme = models.CharField(
        verbose_name="about me",
        max_length=255,
    )
    activation_key = models.CharField(
        verbose_name= 'activation key',
        max_length=40,
        #default = self.activation_key_generator()
        default= gen()
    )


    def del_expired_users(self):
        if self.date_joined - datetime.now() > 7 :
            self.delete(self)
            self.objects.all()


    def activation_key_generator(self):
        salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
        username = self.username
        if isinstance(username, unicode):
            username = username.encode('utf-8')
        activation_key = hashlib.sha1(salt+username).hexdigest()
        self.activation_key = activation_key
        print "alireza"
        return True




'''

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.conf import settings


'''@receiver(pre_save, sender=MyUser)
def mymodel_save_handler(sender, **kwargs):
    #mymodel_save_handler.request.user.is_active = False
    user = kwargs['instance']
    if not user.is_staff :
        user.is_active = False
'''
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail



@receiver(post_save, sender=MyUser)
def mymodel_post_save_handler(sender, **kwargs):
    #mymodel_save_handler.request.user.is_active = False
    user = kwargs['instance']
    ctx_dict = {'activation_key': user.activation_key,
                    'expiration_days': 7,#settings.ACCOUNT_ACTIVATION_DAYS,
                    'site': "mysite.com",
                    'username': user.username }

    subject = render_to_string('main/frontEnd/users/activation_email_subject.txt',
                                   ctx_dict)
    # Email subject *must not* contain newlines
    subject = ''.join(subject.splitlines())

    message = render_to_string('main/frontEnd/users/activation_email.txt',
                            ctx_dict)

    #ser.email_user(subject, message, settings.DEFAULT_FROM_EMAIL)
    send_mail(subject, message, 'YOUR EMAIL',
        [user.email], fail_silently=False)
