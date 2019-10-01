from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*_wzkua(vma=h)9cz$f!*5fj0f760wvus5=(519*9d1i3jg8=+'

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

INTERNAL_IPS = [
    '127.0.0.1',
]

INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
