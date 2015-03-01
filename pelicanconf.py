#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Petr Horáček'
SITENAME = u'Raketomodelářský klub Letovice'
SITENAME_SHORT = u'RMK Letovice'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'cs'

DEFAULT_PAGINATION = 10

# Paths
PATH = 'content'

# Static files
STATIC_DIR = 'theme'
MY_CSS = 'css/style.css'
BOOTSTRAP_CSS = 'css/bootstrap.min.css'
BOOTSTRAP_JS = 'js/bootstrap.min.js'
LOGO = 'images/logo.png'
JUMBOTRON_IMAGE = 'images/top.jpg'

# External resources
JQUERY = 'https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js'
HTML5SHIV = 'https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js'
RESPOND = 'https://oss.maxcdn.com/respond/1.4.2/respond.min.js'

# Content
NAVIGATION_BAR = ({'label': 'Úvod', 'href': '/'},
                  {'label': 'Letové akce', 'href': '', 'actions_list': 'letove-akce'},
                  {'label': 'Fotogalerie', 'href': ''},
                  {'label': 'Historie', 'href': ''})
CONTACTS = ({'name': 'Jan Novák',
             'info': 'titul',
             'phone': 'XXX XXX XXX',
             'mail': ('jan', 'seznam', 'cz')},)

# Jinja filters
def archive_years(dates):
    years = set()
    for d in dates:
        year = d.date.strftime('%Y')
        years.add(year)
    return years

def key_equals(objects, key, param):
    filtered = []
    for o in objects:
        if getattr(o, key) == param:
            filtered.append(o)
    return filtered

JINJA_FILTERS = {'archive_years': archive_years,
                 'key_equals': key_equals}

# Don't want any feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
