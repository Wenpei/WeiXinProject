'''
Created on 2013-5-10

@author: weyu
'''
import logging
import json
from hashlib import md5
from time import time
import tornado

import weather_data_analytic

class HomePage(tornado.web.RequestHandler):
    def __init__(self):
        pass
    def get(self):
        html = weather_data_analytic.getHeader()
        html += weather_data_analytic.getBody("gangu")
        html += weather_data_analytic.getBottom()
        return html

########
'''
urls = [
    (r"/", HomePage),
    (r"/robots.txt", Robots),
    (r"/feed", Feed),
    (r"/index.xml", Feed),
    (r"/t/(\d+)$", PostDetailShort),
    (r"/topic/(\d+)/(.*)$", PostDetail),
    (r"/index_(prev|next)_page/(\d+)/(\d+)/$", IndexPage),
    (r"/c/(\d+)$", CategoryDetailShort),
    (r"/category/(.+)/$", CategoryDetail),
    (r"/tag/(.+)/$", TagDetail),
    (r"/(cat|tag)_(prev|next)_page/(\d+)/(.+)/$", ArticleList),
    (r"/sitemap_(\d+)\.xml$", Sitemap),
    (r"/attachment/(.+)$", Attachment),
]'''

urls = [
        (r"/",HomePage),
        ]