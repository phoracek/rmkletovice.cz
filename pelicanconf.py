#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import ast
import sys
reload(sys)
sys.setdefaultencoding('utf8')

AUTHOR = u'Petr Horáček'
SITENAME = u'Raketomodelářský klub Letovice'
SITENAME_SHORT = u'RMK Letovice'
SITEURL = ''

TIMEZONE = 'Europe/Prague'

DEFAULT_LANG = u'cs'

DEFAULT_PAGINATION = 10

DEFAULT_CATEGORY = 'Ostatní'

FILENAME_METADATA = '(?P<date>\d{4}\d{2}\d{2})-(?P<slug>.*)'

# Paths
PATH = 'content'
ARTICLE_URL = 'clanky/{category}/{slug}.html'
ARTICLE_SAVE_AS = 'clanky/{category}/{slug}.html'
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'
CATEGORY_URL = 'kategorie/{slug}.html'
CATEGORY_SAVE_AS = 'kategorie/{slug}.html'
CATEGORY_PAGINATION_URL = 'kategorie/{slug}-{page}.html'
CATEGORY_PAGINATION_SAVE_AS = 'kategorie/{slug}-{page}.html'

# Plugins
PLUGIN_PATHS = ('plugins',)
PLUGINS = ('archives_per_category',)

# Archives
ARCHIVE_DIR = 'archiv'
ARCHIVE_YEARS = range(2017, 2014, -1)
YEAR_ARCHIVE_SAVE_AS = ARCHIVE_DIR + '/{date:%Y}/index.html'
YEAR_ARCHIVES_PER_CATEGORY_SAVE_AS = (ARCHIVE_DIR +
                                      '/{category}/{date:%Y}/index.html')
CATEGORIES_TO_ARCHIVE = ('letove-akce',)

# Static files
STATIC_PATHS = ['docs']
STATIC_DIR = 'theme'
MY_CSS = 'css/style.css'
BOOTSTRAP_CSS = 'css/bootstrap.min.css'
BOOTSTRAP_JS = 'js/bootstrap.min.js'
LOGO = FAVICON = 'images/logo.png'
JUMBOTRON_IMAGE_MAX = 'images/top_max.jpg'
JUMBOTRON_IMAGE_2560 = 'images/top_2560.jpg'
JUMBOTRON_IMAGE_1920 = 'images/top_1920.jpg'
JUMBOTRON_IMAGE_1366 = 'images/top_1366.jpg'
JUMBOTRON_IMAGE_1280 = 'images/top_1280.jpg'
JUMBOTRON_IMAGE_1024 = 'images/top_1024.jpg'
JUMBOTRON_IMAGE_800 = 'images/top_800.jpg'

# External resources
JQUERY = 'https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js'
HTML5SHIV = 'https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js'
RESPOND = 'https://oss.maxcdn.com/respond/1.4.2/respond.min.js'

# Content
WELCOME_MESSAGE = 'Vítejte na stránkách Raketomodelářského klubu Letovice'
NAVIGATION_BAR = ({'label': 'Úvod', 'href': '/'},
                  {'label': 'Letové akce',
                   'href': '/kategorie/letove-akce.html',
                   'actions_list': [
                       (year, '/%s/letove-akce/%d' % (ARCHIVE_DIR, year))
                       for year in range(2017, 2014, -1)
                   ]},
                  {'label': 'Fotogalerie',
                   'href': 'https://www.zonerama.com/rmkletovice',
                   'target': '_blank'},
                  {'label': 'Historie', 'href': '/historie-klubu.html'})
CONTACTS = ({'name': 'Jiří Kašpar',
             'info': 'předseda klubu',
             'phone': '606 803 431',
             'mail': ('kasparj45', 'seznam', 'cz')},
            {'name': 'Petr Horáček',
             'info': 'správce webu',
             'mail': ('p.horacek94', 'gmail', 'com')})


# Jinja filters
def key_equals(objects, key, param):
    filtered = []
    for o in objects:
        if getattr(o, key) == param:
            filtered.append(o)
    return filtered


def parse_structure(string):
    return ast.literal_eval(string)


JINJA_FILTERS = {'key_equals': key_equals,
                 'parse_structure': parse_structure}

# Don't want any feeds
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
