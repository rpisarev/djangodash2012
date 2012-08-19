import os
DEBUG = True
TEMPLATE_DEBUG = True

PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(PROJECT_ROOT, '../db.sqlite'),                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    },
}

PARSE_GOOGLE_COUNT = 20 #count google images
PARSE_INSTAGRAM_COUNT = 8 #count instagram iteration
PARSE_FLICKR_COUNT = 150 # count flickr photo