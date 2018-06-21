# -*- coding:utf-8 -*-
import urllib2, sys

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return

        # 模拟浏览器可以加快爬取速度
        req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36')

        response = urllib2.urlopen(req, timeout = 5)

        #response = urllib2.urlopen(url)

        if response.getcode() != 200:
            return None
        else:
            return response.read()
