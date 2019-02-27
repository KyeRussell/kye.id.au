import os

AUTHOR = 'Kye Russell'
SITENAME = 'Kye Russell'
SITEURL = 'https://www.kye.id.au'

PATH = 'content'

TIMEZONE = 'Australia/Perth'

DEFAULT_LANG = 'en'

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['sitemap']


# Customise URLs

ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
ARTICLE_URL = 'blog/{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'


# Disable unused pages.

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
ARTICLE_LANG_SAVE_AS = ''
DRAFT_SAVE_AS = ''
DRAFT_LANG_SAVE_AS = ''
PAGE_LANG_SAVE_AS = ''
DRAFT_PAGE_SAVE_AS = ''
DRAFT_PAGE_LANG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
TAGS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''


# Theme

THEME = 'theme'


# Sitemap

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1.0,
        'pages': 0.9,
        'indexes': 0.8,
    },
    'changefreqs': {
        'articles': 'weekly',
        'pages': 'weekly',
        'indexes': 'weekly'
    },
}

ENVIRONMENT = os.environ.get('PELICAN_ENVIRONMENT', 'development')

if ENVIRONMENT == 'development':
    RELATIVE_URLS = True
