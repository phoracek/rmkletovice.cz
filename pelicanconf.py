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

DEFAULT_CATEGORY = 'ostatni'

# Paths
PATH = 'content'

# Plugins
PLUGIN_PATHS = ('plugins',)
PLUGINS = ('archives_per_category',)

# Archives
ARCHIVE_DIR = 'archiv'
ARCHIVE_YEARS = ('2011', '2010')
YEAR_ARCHIVE_SAVE_AS = ARCHIVE_DIR + '/{date:%Y}/index.html'
YEAR_ARCHIVES_PER_CATEGORY_SAVE_AS = (ARCHIVE_DIR +
                                      '/{category}/{date:%Y}/index.html')
CATEGORIES_TO_ARCHIVE = ('letove-akce',)

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
WELCOME_MESSAGE = 'Vítejte na stránkách Raketomodelářského klubu Letovice'
NAVIGATION_BAR = ({'label': 'Úvod', 'href': '/'},
                  {'label': 'Letové akce', 'href': '/category/letove-akce.html',
                        'actions_list': (('2010', ARCHIVE_DIR + '/letove-akce/2010'),)},
                  {'label': 'Fotogalerie', 'href': ''},
                  {'label': 'Historie', 'href': '/pages/historie-klubu.html'})
CONTACTS = ({'name': 'Jan Novák',
             'info': 'titul',
             'phone': 'XXX XXX XXX',
             'mail': ('jan', 'seznam', 'cz')},)

# Jinja filters
def key_equals(objects, key, param):
    filtered = []
    for o in objects:
        if getattr(o, key) == param:
            filtered.append(o)
    return filtered

import ast
def parse_structure(string):
    return ast.literal_eval(string)

from datetime import datetime
def parse_and_format_date(string):
    new = datetime.strptime(string, '%Y-%m-%d').strftime('%-d. %-m. %Y')
    return new

JINJA_FILTERS = {'key_equals': key_equals,
                 'parse_structure': parse_structure,
                 'parse_and_format_date': parse_and_format_date}

# Don't want any feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
