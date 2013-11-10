# -*- coding: utf-8 -*-
import os

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'https://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}
]

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# administrator list
ADMINS = ['you@example.com']

# For pagination
POSTS_PER_PAGE = 3

# For full-text search
WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 50

# E-Mail server
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = ''
MAIL_PASSWORD = ''

# administrator list
ADMINS = ['']

# Available languages
LANGUAGES = {
    'en': 'English',
    'es': 'Español'
}

MS_TRANSLATOR_CLIENT_ID='ee6ba84b-9a3c-43b3-a265-55fbfa778c8b'
MS_TRANSLATOR_CLIENT_SECRET='AyIkB62OPDArWu1ks0j3UQXsbgbmTj6HvbOXaKk7JUo='