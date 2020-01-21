#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Alexander Gonser'
SITENAME = 'Alexander Gonser'
SITEURL = ''

# Content Paths
PATH = 'content'
ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['img', 'pdf']
PAGE_PATHS = ['pages']

TIMEZONE = 'America/Detroit'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Royal Oak Coffee House Coders', 'http://royaloak.coffeehousecoders.com/'),
         ('Michigan!/usr/group', 'https://mug.org'),
         ('RSS', 'feeds/all.atom.xml'),)

# Social widget
SOCIAL = (('Facebook', 'https://facebook.com/agonser'),
          ('Github', 'https://github.com/mechpilotace'),
          ('YouTube', 'https://www.youtube.com/channel/UCqJsSnO9gD935ShY46dWazA'),
          ('Mastodon - TBD', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme Settings
THEME = 'theme'
PLUGIN_PATH = ['plugins/', ]
PLUGINS = ['i18n_subsites', ]
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n']
}
BOOTSTRAP_THEME = 'cyborg'
PYGMENTS_STYLE = 'monokai'

# URL Formatting
ARTICLE_URL = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS_URL = 'pages/{slug}/index.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
