# Django settings for example project.
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = ''

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'wobwwik!&)qmyt2kf3(^jjc6gff)jbtuir+&2)ux7e#xozf5@m'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    "templates",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',

    'app',
    'billing',
    'stripe',
    'paypal.pro',
    'crispy_forms',
    'raven.contrib.django.raven_compat'
)

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(os.path.dirname(__file__), "static")
STATICFILES_FINDER = ("django.contrib.staticfiles.finders.FileSystemFinder",
                      "django.contrib.staticfiles.finders.AppDirectoriesFinder")
USE_TZ = True
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

ALLOWED_HOSTS = ['agiliq.com']
# MERCHANT SETTINGS
MERCHANT_TEST_MODE = True
# MERCHANT_SETTINGS = get_merchant_settings()
MERCHANT_SETTINGS = {
    # AUTHORIZE.NET SETTINGS
    "authorize_net": {
        "LOGIN_ID" : '',
        "TRANSACTION_KEY" : '',
        "MD5_HASH": ''
        },

    # PAYPAL SETTINGS
    "pay_pal": {
        "WPP_USER":"anastasiia-facilitator_api1.timebridge.com",
        "WPP_PASSWORD":"SD94B46FZQQCXQYA",
        "WPP_SIGNATURE":"AW9Y2geFfmCfJS5fGBN7B-KnnviQAoDHA8YlYIOJDl30w7tljJ9wuQDN",
        "RECEIVER_EMAIL": "anastasiia@timebridge.com"
    },

    # EWAY SETTINGS
    "eway": {
        "CUSTOMER_ID" : '',
        "USERNAME" : '',
        "PASSWORD" : '',
        },

    # WORLDPAY settings
    "world_pay": {
        "HOSTED_URL_TEST" : "https://select-test.wp3.rbsworldpay.com/wcc/purchase",
        "HOSTED_URL_LIVE" : "https://secure.wp3.rbsworldpay.com/wcc/purchase",
        "INSTALLATION_ID_TEST" : '',
        "INSTALLATION_ID_LIVE" : '',
        "MD5_SECRET_KEY" : ''
        },

    # Amazon FPS settings
    "amazon_fps": {
        "AWS_ACCESS_KEY" : '',
        "AWS_SECRET_ACCESS_KEY" : ''
        },

    # Braintree Payment settings
    "braintree_payments": {
        "MERCHANT_ACCOUNT_ID" : "",
        "PUBLIC_KEY" : "",
        "PRIVATE_KEY" : ""
        },

    # Stripe Payment Settings
    "stripe": {
        "API_KEY" : 'sk_test_4H6NIBCw57iufW8pGi0Efg7a',
        "PUBLISHABLE_KEY" : 'pk_test_XCutYAKOng3R63LJpRoE9SaT'
        },

    # Paylane Settings
    "paylane": {
        "USERNAME": "",
        "PASSWORD": ""
        },

    # WePay Settings
    "we_pay": {
        "CLIENT_ID": "",
        "CLIENT_SECRET": "",
        # Below two are optional if are passed as
        # extra option items. Useful for marketplace
        "ACCOUNT_ID": "",
        "ACCESS_TOKEN": "",
        },

    "beanstream": {
        "MERCHANT_ID": "",
        "LOGIN_COMPANY": "",
        "LOGIN_USER": "",
        "LOGIN_PASSWORD": "",
        # Below two are optional
        "HASH_ALGORITHM"   : "",
        "HASHCODE"  : ""
    },

    "chargebee": {
        "API_KEY": "",
        "SITE": ""
    },

    "bitcoin": {
        "RPCUSER": "",
        "RPCPASSWORD": "",
        "HOST": "",
        "PORT": "",
        "ACCOUNT": "",
        "MINCONF": 1,
    },

    "ogone_payments": {
        "SHA_PRE_SECRET": '',
        "SHA_POST_SECRET": '',
        "HASH_METHOD": 'sha512',
        "PRODUCTION": not MERCHANT_TEST_MODE,
        "PSPID": 'mypspid',
        "OGONE_TEST_URL": 'https://secure.ogone.com/ncol/test/orderstandard.asp',
        "OGONE_PROD_URL": 'https://secure.ogone.com/ncol/prod/orderstandard.asp'
    },

    "pin": {
        "SECRET": ""
    }
}
# PAYPAL SETTINGS
if MERCHANT_SETTINGS.get("pay_pal"):
    PAYPAL_TEST = MERCHANT_TEST_MODE
    PAYPAL_WPP_USER = MERCHANT_SETTINGS["pay_pal"]["WPP_USER"]
    PAYPAL_WPP_PASSWORD = MERCHANT_SETTINGS["pay_pal"]["WPP_PASSWORD"]
    PAYPAL_WPP_SIGNATURE = MERCHANT_SETTINGS["pay_pal"]["WPP_SIGNATURE"]
    PAYPAL_RECEIVER_EMAIL = MERCHANT_SETTINGS["pay_pal"]["RECEIVER_EMAIL"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'merchant.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
ADMIN_MEDIA_PREFIX = "/static/admin/"
