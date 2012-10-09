import dj_database_url
DATABASES = {'default': dj_database_url.config(default='postgres://localhost')}

DEBUG = True
ASSETS_DEBUG = True
STATIC_URL = '/static/'



