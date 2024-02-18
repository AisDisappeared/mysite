from mysite.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-zh2+bchkbx6wt@e*#eqz0fj7#vpq20=$s(k&%zv9k*-nr7_#kj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['disapp.ir','www.disapp.ir']



# sites framework 
SITE_ID = 2



# apps that are installed at django 
# INSTALLED_APPS = []





# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# static and media roots settings 
STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / "statics",
]



# Cookie settings
CSRF_COOKIE_SECURE = True 



# django compressor setting  when we are at production virtual 
COMPRESS_ENABLED = True
COMPRESS_ROOT = STATIC_ROOT ##django compressor
COMPRESS_OFFLINE = True

if not COMPRESS_ENABLED: ##django compressor
    COMPRESS_ENABLED = True
    COMPRESS_CSS_FILTERS = ["compressor.filters.cssmin.CSSMinFilter"]
    COMPRESS_JS_FILTERS = ["compressor.filters.jsmin.JSMinFilter"] ##django compressor
