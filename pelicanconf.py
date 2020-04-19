#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Satyakam Goswami'
SITENAME = u'Satyaakam.net'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),)

#Variable to set Theme
THEME = './Flex'

SITESUBTITLE ='Learning and Living'
SITETAG = "Satyaakam.net"

# Extra stylesheets, for bootstrap overrides or additional styling.
STYLESHEET_FILES = ("pygment.css", "voidybootstrap.css",)

# Put taglist at end of articles, and use the default sharing button implementation.
CUSTOM_ARTICLE_FOOTERS = ("taglist.html", "sharing.html", )
CUSTOM_SCRIPTS_ARTICLE = "sharing_scripts.html"

# Default sidebar template. Omit this line for single column mode without sidebar.
SIDEBAR = "sidebar.html"

SOCIAL = (('Google+', 'http://plus.google.com/satyaakam'),
        ('Twitter', 'https://twitter.com/satyaakam'),
        ('LinkedIn', 'https://www.linkedin.com/in/satyaakam'),
        ('BitBucket', 'http://bitbucket.org/satyaakam'),
        ('GitHub', 'http://github.com/satyaakam'),
        )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 'CNAME', 'id_rsa.pub.txt']
JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}
