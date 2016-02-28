# -*- coding: utf8 -*-
#
# Django settings for biostar project.
#
from __future__ import absolute_import
import os
from django.core.exceptions import ImproperlyConfigured
from .logger import LOGGING

# Turn off debug mode on deployed servers.
DEBUG = True


# Should the django compressor be used.
USE_COMPRESSOR = False

# The start categories. These tags have special meaning internally.
START_CATEGORIES = [
    "Latest",  "Open",
]

# These should be the most frequent (or special) tags on the site.
NAVBAR_TAGS = [
    "RNA-Seq", "ChIP-Seq", "SNP", "Assembly",
]

# The last categories. These tags have special meaning internally.
END_CATEGORIES = [
    "Tutorials", "Tools",  "Jobs", "Forum",
]

# These are the tags that always show up in the tag recommendation dropdown.
POST_TAG_LIST = NAVBAR_TAGS + ["software error"]

# This will form the navbar
CATEGORIES = START_CATEGORIES + NAVBAR_TAGS + END_CATEGORIES

# This will appear as a top banner.
# It should point to a template that will be included.
TOP_BANNER = ""

#TOP_BANNER = "test-banner.html"

def get_env(name, func=None):
    """Get the environment variable or return exception"""
    try:
        if func:
            return func(os.environ[name])
        else:
            return unicode(os.environ[name], encoding="utf-8")
    except KeyError:
        msg = "*** Required environment variable %s not set." % name
        raise ImproperlyConfigured(msg)

def abspath(*args):
    """Generates absolute paths"""
    return os.path.abspath(os.path.join(*args))

# Displays debug comments when the server is run from this IP.
INTERNAL_IPS = ('127.0.0.1', )

# Set location relative to the current file directory.
HOME_DIR = get_env("BIOSTAR_HOME")
LIVE_DIR = abspath(HOME_DIR, 'live')

DATABASE_NAME = abspath(LIVE_DIR, get_env("DATABASE_NAME"))
STATIC_DIR = abspath(HOME_DIR, 'biostar', 'static')
TEMPLATE_DIR = abspath(HOME_DIR, 'biostar', 'server', 'templates')

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
EXPORT_DIR = abspath(LIVE_DIR, "export")
STATIC_ROOT = abspath(EXPORT_DIR, "static")

# This is where the planet files are collected
PLANET_DIR = abspath(LIVE_DIR, "planet")

# Absolute filesystem path to the directory that will hold user-uploaded files.
MEDIA_ROOT = abspath(EXPORT_DIR, "media")

# Needs to point to the directory that contains the
# html files that are stored in the flatpages about, faq, help, policy etc.
FLATPAGE_IMPORT_DIR = abspath(HOME_DIR, "import", "pages")

# Default search index location.
WHOOSH_INDEX = abspath(LIVE_DIR, "whoosh_index")

# These settings create an admin user.
# The default password is the SECRET_KEY.
ADMIN_NAME = get_env("BIOSTAR_ADMIN_NAME")
ADMIN_EMAIL = get_env("BIOSTAR_ADMIN_EMAIL")
ADMIN_LOCATION = "State College, USA"
ADMINS = (
    (ADMIN_NAME, ADMIN_EMAIL),
)

# Get the secret key from the environment.
SECRET_KEY = get_env("SECRET_KEY")

MANAGERS = ADMINS

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATABASE_NAME,
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}


# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost", "www.lvh.me", get_env("BIOSTAR_HOSTNAME")]

ATOMIC_REQUESTS = True
CONN_MAX_AGE = 10;

# Allowed html content.
ALLOWED_TAGS = "p div br code pre h1 h2 h3 h4 hr span s sub sup b i img strong strike em underline super table thead tr th td tbody".split()
ALLOWED_STYLES = 'color font-weight background-color width height'.split()
ALLOWED_ATTRIBUTES = {
    '*': ['class', 'style'],
    'a': ['href', 'rel'],
    'img': ['src', 'alt', 'width', 'height'],
    'table': ['border', 'cellpadding', 'cellspacing'],

}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# Configure language detection
LANGUAGE_DETECTION = ['en']

# These parameters will be inserted into the database automatically.
SITE_ID = 1
SITE_NAME = "Site Name"
SITE_DOMAIN = get_env("BIOSTAR_HOSTNAME")

SERVER_EMAIL = DEFAULT_FROM_EMAIL = get_env("DEFAULT_FROM_EMAIL")

# What domain will handle the replies.
EMAIL_REPLY_PATTERN = "reply+%s+code@biostars.io"

# The format of the email that is sent
EMAIL_FROM_PATTERN = u'''"%s on Biostar" <%s>'''

# The secret key that is required to parse the email
EMAIL_REPLY_SECRET_KEY = "abc"

# The subject of the reply goes here
EMAIL_REPLY_SUBJECT = u"[biostar] %s"

# Should replying to an email remove the quoted text
EMAIL_REPLY_REMOVE_QUOTED_TEXT = True

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True


# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/static/upload/'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Use absolute paths, not relative paths.
    STATIC_DIR,
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'biostar.server.middleware.Visit',
)

ROOT_URLCONF = 'biostar.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'biostar.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ TEMPLATE_DIR],
        'TEMPLATE_DEBUG': DEBUG,
        'TEMPLATE_STRING_IF_INVALID': "*** MISSING ***",
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'biostar.server.context.shortcuts',
            ],
        },
    },
]

# The user score that halves the chance.
HALF_LIFE = 30.0

LOGIN_REDIRECT_URL = "/"

MESSAGE_TAGS = {
    10: 'alert-info', 20: 'alert-info',
    25: 'alert-success', 30: 'alert-warning', 40: 'alert-danger',
}

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',

    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',

    # The javascript and CSS asset manager.
    'compressor',

    # Enabling the admin and its documentation.
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.flatpages',
    'django.contrib.sessions',

    # Biostar specific apps.
    'biostar.apps.users',
    'biostar.apps.util',
    'biostar.apps.posts',
    'biostar.server.apps.MessageConfig',
    'biostar.apps.badges',
    'biostar.apps.planet',

    # The main Biostar server.
    'biostar.server',

    # Social login handlers.
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.persona',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    #'allauth.socialaccount.providers.facebook',
    #'allauth.socialaccount.providers.orcid',
    #'allauth.socialaccount.providers.linkedin',
    #'allauth.socialaccount.providers.weibo',

    # External apps.
    'haystack',
    'crispy_forms',
    'djcelery',
    'kombu.transport.django',
    'captcha',
]

CRISPY_TEMPLATE_PACK = 'bootstrap3'

AUTH_USER_MODEL = 'users.User'

DEBUG_TOOLBAR_PATCH_SETTINGS = False

# Default search is provided via Whoosh

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': WHOOSH_INDEX,
    },
}

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "biostar.server.middleware.ExternalAuth",
)


# Should the captcha be shown on the signup page.
CAPTCHA = True

# For how long does a user need to be a member to become trusted.
TRUST_RANGE_DAYS = 7

# Votes needed to start trusting the user
TRUST_VOTE_COUNT = 5

# How many non top level posts per day for users.
MAX_POSTS_NEW_USER = 5
MAX_POSTS_TRUSTED_USER = 30

# How many top level posts per day for a new user.
MAX_TOP_POSTS_NEW_USER = 2
MAX_TOP_POSTS_TRUSTED_USER = 5

# The google id will injected as a template variable.
GOOGLE_TRACKER = ""
GOOGLE_DOMAIN = ""

# The site logo.
SITE_LOGO = "biostar2.logo.png"

# Digest title
DAILY_DIGEST_TITLE = '[biostar daily digest] %s'
WEEKLY_DIGEST_TITLE = '[biostar weekly digest] %s'


# The default CSS file to load.
SITE_STYLE_CSS = "biostar.style.less"

# Set it to None if all posts should be accesible via the Latest tab.
SITE_LATEST_POST_LIMIT = None

# How many recent objects to show in the sidebar.
RECENT_VOTE_COUNT = 7
RECENT_USER_COUNT = 7
RECENT_POST_COUNT = 12

# Time between two accesses from the same IP to qualify as a different view.
POST_VIEW_MINUTES = 5

# Default  expiration in seconds.
CACHE_TIMEOUT = 60

# Should the messages go to email by default
# Valid values are local, default, email
DEFAULT_MESSAGE_PREF = "local"

# Django precompressor settings.
COMPRESS_PRECOMPILERS = (
    ('text/coffeescript', 'coffee --compile --stdio'),
    ('text/less', 'lessc {infile} {outfile}'),
)

COMPRESS_OFFLINE_CONTEXT = {
    'STATIC_URL': STATIC_URL,
    'SITE_STYLE_CSS': SITE_STYLE_CSS,
}

# The cache mechanism is deployment dependent. Override it externally.
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache' if DEBUG else 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake'
    }
}

# The celery configuration file
CELERY_CONFIG = 'biostar.celeryconfig'

# Setting a cookie with email:signed_hash(email)
# will automatically create accounts
EXTERNAL_AUTH = [
    ("foo.bar.com", "ABC"),
]

# Set these to redirect login to an external site.
EXTERNAL_LOGIN_URL = None
EXTERNAL_SIGNUP_URL = None
EXTERNAL_LOGOUT_URL = None
EXTERNAL_SESSION_KEY = "EXTERNAL"
EXTERNAL_SESSION_FIELDS = "title tag_val content".split()

# How far to look for posts for anonymous users.
COUNT_INTERVAL_WEEKS = 10000

# How frequently do we update the counts for authenticated users.
SESSION_UPDATE_SECONDS = 10 * 60
SESSION_COOKIE_NAME = "biostar2"

# The number of posts to show per page.
PAGINATE_BY = 25

# Used by crispyforms.
#CRISPY_FAIL_SILENTLY = not DEBUG

ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_EMAIL_VERIFICATION = "optional"
ACCOUNT_EMAIL_SUBJECT_PREFIX = "[biostar] "
ACCOUNT_PASSWORD_MIN_LENGHT = 6
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USER_MODEL_EMAIL_FIELD = "email"
ACCOUNT_DEFAULT_HTTP_PROTOCOL = "http"
#ACCOUNT_LOGOUT_ON_GET = True

# Google ReCaptcha No-Captcha settings
# When set the captcha forms will be active.
RECAPTCHA_PUBLIC_KEY = ""
RECAPTCHA_PRIVATE_KEY = ""
RECAPTCHA_USE_SSL = True     # Defaults to False
NOCAPTCHA = True

# Session specific settings.
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
SESSION_KEY = "session"

# Use a mock email backend for development.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# On deployed servers the following must be set.
EMAIL_HOST = get_env("EMAIL_HOST")
EMAIL_PORT = get_env("EMAIL_PORT", func=int)
EMAIL_HOST_USER = get_env("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = get_env("EMAIL_HOST_PASSWORD")
