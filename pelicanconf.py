#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import webassets
import jinja2
from jinja2 import environment
import jinja2.ext
from jinja2.ext import loopcontrols
from jinja2.ext import i18n
from jinja2.ext import with_
from jinja2.ext import do


AUTHOR = 'Dan'
SITENAME = 'Dan Decker'
SITESUBTITLE = 'A Semi-Pro Blog'
SITEURL = 'https://dandecker.us'

PATH = 'content'
PAGE_PATHS = ['Pages']
ARTICLE_PATHS= ['Articles']
OUTPUT_PATH = 'output'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
MENUITEMS = ( #('Pelican', 'http://getpelican.com/'),
              #('Python.org', 'http://python.org/'),
              ('Anaconda Python', 'https://www.anaconda.com/distribution/'),
              ('GitHub', 'https://github.com/therealdandecker'),
              ('Jinja2', 'http://jinja.pocoo.org/'),
              ('LinkedIn', 'https://www.linkedin.com/in/dan-d-789a1ab/'),
              ('Resume', 'https://dandecker.us/pdfs/Resume.pdf'),
              ('Tableau Public','https://public.tableau.com/profile/dan.decker#!/')
          )

# Pagination
DEFAULT_PAGINATION = 5
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['assets','pdfs']
#ARTICLE_PATHS = ['content']
PLUGIN_PATHS = [
  'pelican-plugins'
]

PLUGINS = [
  'sitemap',
  'neighbors',
  'assets'
]

# Sitemap
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}



# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

HOME_COVER = 'theme/images/home-bg.jpg'

HEADER_COVERS_BY_TAG = {'blog': 'theme/images/post-bg.jpg'}

THEME ="attila"

# Post and Pages path
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Tags and Category path
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_SAVE_AS = 'catgegories.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_SAVE_AS = 'tags.html'

# Author
AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_SAVE_AS = 'authors.html'

AUTHORS_BIO = {
  "dan": {
    "name": "Dan",
    "website": "https://dandecker.us",
    "linkedin": "https://www.linkedin.com/in/dan-d-789a1ab/",
    "github": "https://github.com/therealdandecker",
    "location": "USA",
    "cover": "theme/images/about-bg.jpg",
    "image": "theme/images/Data.png",
    "bio": "Dan Decker is not an award winning novelist, but they will let anyone with Python skills make a website these days."
  }
}

JINJA_ENVIRONMENT = {
  'extensions' :[
    'jinja2.ext.loopcontrols',
    'jinja2.ext.i18n',
    'jinja2.ext.with_',
    'jinja2.ext.do'
  ]
}

JINJA_FILTERS = {'max': max}