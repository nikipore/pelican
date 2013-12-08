#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://staging.luftmensch.net.s3-website-eu-west-1.amazonaws.com'

RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

#ADDTHIS_PROFILE = 'luftmensch'
DISQUS_SITENAME = 'staging.luftmensch'
#GOOGLE_ANALYTICS = 'UA-40656153-1'
