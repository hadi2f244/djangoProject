# Django settings for mainProject project.

import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG
#testing

mainPath=os.getcwd()

SITE_NAME="test1.com:8000" #we use this in subdomainMiddleware

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(mainPath, "mainProject.db"),# Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []
#there is just a test
#another test
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'fa_IR'
SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

#LOCALE_PATHS =  ("/home/hadi2f244/codes/djangoMain2/locale",)
_ = lambda s: s

LANGUAGES = (
  ('fa', _('Persian')),
  ('en', _('English')),
)


#LOCALE_PATHS=( mainPath + 'locale',)
LOCALE_PATHS = (
    os.path.join(mainPath, "locale"),
    "/usr/local/lib/python2.7/dist-packages/django/contrib/auth/locale",
)
ADMIN_LANGUAGE_CODE = 'fa-IR'
# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(mainPath, "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    #('assets',os.path.join(os.path.dirname(__file__), 'static')),
    ('blogStatic',os.path.join(mainPath, "static/blog/assets")),
    ('mainStatic',os.path.join(mainPath, "static/main/assets")),
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#   'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'h$_h5gr5o8&w_$yt^1um3q-g=f%4!8y4%%j67ri^-i)@rgs^00'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    #'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
)

MIDDLEWARE_CLASSES = (
    'mainProject.middleware.SubdomainSet',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    #Uncomment the next line for simple clickjacking protection:
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'mainProject.adminLocalMiddleware.AdminLocaleMiddleware',



)

X_FRAME_OPTIONS='DENY' #config of clickjacking middleware


ROOT_URLCONF='mainProject.urls' #this is just for error solving ! but we set this in subdomainset middleware from ROOT_URLCONFDICT

ROOT_URLCONFDICT ={
    'mainProject':'mainProject.urls',
    'blog':'blog.urls',
}


# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'mainProject.wsgi.application'



TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    #os.path.join(mainPath,'blog', "templates"),
    os.path.join(mainPath, "templates"),

    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'dajaxice.finders.DajaxiceFinder',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    'django.contrib.admindocs',
    # This is for searching
    #'registration',
    'user',
    'haystack',
    'backEnd',
    'blog',
    'blog.article',
    'blog.category',
    'blog.backEnd',
    'ckeditor',
    #'django_markdown',
    'dajaxice',
    'south',
    'django_bleach',
    'new',

)
ACCOUNT_ACTIVATION_DAYS = 7

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
AUTH_USER_MODEL= 'user.MyUser'



# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

CKEDITOR_UPLOAD_PATH = os.path.join(MEDIA_ROOT, "blog/uploads")  # don't touch it is for uploading :)
CKEDITOR_RESTRICT_BY_USER = True

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
        'height': 300,
        'width': 500,
    },
    'simple': {
        'toolbar': 'Basic',
        'height': 300,
        'width': 500,
},

}

# Which HTML tags are allowed
BLEACH_ALLOWED_TAGS = ['h1','h2','h3','h4','h5','h6','pre','p', 'b', 'i', 'u', 'em', 'strong','big', 'a','strike', 'ul', 'li', 'ol', 'br',
                     'span', 'blockquote', 'hr', 'img','table','tbody','td','tr','div','span','small','tt']


# Which HTML attributes are allowed
BLEACH_ALLOWED_ATTRIBUTES = ['href', 'title', 'style','src', 'alt','align','border','cellpadding','cellspacing',"dir"]

# Which CSS properties are allowed in 'style' attributes (assuming style is
# an allowed attribute)
BLEACH_ALLOWED_STYLES = [
    'font-family', 'font-weight', 'text-decoration', 'font-variant','color', 'cursor', 'float', 'margin','width','height','background','padding','background-color']

# Strip unknown tags if True, replace with HTML escaped characters if False
BLEACH_STRIP_TAGS = True

# Strip HTML comments, or leave them in.
BLEACH_STRIP_COMMENTS = False

BLEACH_DEFAULT_WIDGET = 'ckeditor.widgets.CKEditorWidget'

### For smtp server and sending activation email
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'hadi2f2@gmail.com'
EMAIL_HOST_PASSWORD = ''
ACCOUNT_ACTIVATION_DAYS = 7
