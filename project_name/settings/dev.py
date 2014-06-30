# Django project environment-specific settings

from {{ project_name }}.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SITE_ID = 1

#TODO: replace localhost with the domain name of the site
DEFAULT_FROM_EMAIL = 'messenger@localhost'
SERVER_EMAIL = DEFAULT_FROM_EMAIL

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                       # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                       # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                       # Set to empty string for default.
    }
}


TIME_ZONE = 'Canada/Eastern'

INTERNAL_IPS = ('127.0.0.1', )

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Overwrite default ROOT_URLCONF to include static file serving by Django.
# In production, this should be handled separately by your webserver or CDN.
ROOT_URLCONF = '{{ project_name }}.urls.dev'

CDN_FINDER_DIR = os.path.join(PROJECT_ROOT, 'assets')
CDN_FINDER_PREFIX ='http://libs.useso.com/'

INSTALLED_APPS +=('cdn_finder',)

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
        },
       'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'cdn_finder.templatetags.cdn_finder_tags': {
            'handlers': ['console'],
            'level': 'DEBUG'
        },
    }
}