# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import re
import urlparse

class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # forum-58-1.html
        links = soup.find_all('a', href=re.compile(r"forum-\d+-\d+\.htm"))
        for link in links:
            new_url = link['href']

            pattern = re.compile(r'\d+')
            title = link.get_text()
            match = pattern.match(title)

            if match:
                # 将new_url按照page_url的格式拼接成一个新的url
                new_full_url = urlparse.urljoin(page_url, new_url)
                new_urls.add(new_full_url)

        # 新作连发的网页也需要爬取 thread-6723537-1-1.html .*新作\d+連發.*
        links = soup.find_all('a', href=re.compile(r"thread-\d+-\d+-\d+\.html"))
        for link in links:
            # 如果title为空字符串，跳过本次
            title = link.get_text()
            if not title.strip():
                continue

            # 中文必须转码，否则无法匹配.
            keyWord1 = u'新作'
            keyWord2 = u'連發'
            num = r'\d+'
            # .匹配任意字符，包括空格，*表示重复前面的字符0到多个
            pattern = re.compile('.*' + keyWord1 + num + keyWord2 + '.*')
            match = pattern.match(title)

            if match:
                new_url = link['href']
                # 将new_url按照page_url的格式拼接成一个新的url
                new_full_url = urlparse.urljoin(page_url, new_url)
                new_urls.add(new_full_url)

        return new_urls

    def _get_new_data(self, page_url, soup):
        res_datas = []

        # 中文必须转码，否则无法匹配.
        keyWorld = u'仲村茉莉恵'
        # .匹配任意字符，包括空格，*表示重复前面的字符0到多个
        pattern = re.compile('.*' + keyWorld + '.*')

        pattern1 = re.compile(r'http://67.220.90.12/bbs/forum-\d+-\d+.html')
        match1 = pattern1.match(page_url)
        if match1:
            # thread-6723537-1-1.html
            links = soup.find_all('a', href=re.compile(r"thread-\d+-\d+-\d+\.html"))
            for link in links:
                # 如果title为空字符串，跳过本次
                title = link.get_text()
                if not title.strip():
                    continue
                
                match = pattern.match(title)

                if match:
                    data = {}

                    new_url = link['href']
                    # 将new_url按照page_url的格式拼接成一个新的url
                    new_full_url = urlparse.urljoin(page_url, new_url)
                    data['url'] = new_full_url

                    data['title'] = title

                    # 如果找到匹配项，直接在屏幕上打印出来
                    print new_full_url + ' ' + title

                    res_datas.append(data)

        # 查找新作连发页中匹配项
        pattern2 = re.compile(r'http://67.220.90.12/bbs/thread-\d+-\d+-\d+.html')
        match2 = pattern2.match(page_url)
        if (match2):
            # 是新作连发页，查找里面是否有匹配项，如果有，就返回新作连发页地址及标题
            # <td class=postcontent> <div class=postmessage defaultpost>  <div id=postmessage_\d+, class=c>
            content_node = soup.find('div', class_='t_msgfont')
            content = content_node.get_text()
            content = ''.join(content.split())
            # print 'new work: ' + content

            match = pattern.match(content)

            if match:
                data = {}

                data['url'] = page_url

                # postmessage defaultpost
                title = soup.find('div', class_='postmessage defaultpost').find('h2').get_text()
                data['title'] = title

                print page_url + ' ' + title

                res_datas.append(data)

        return res_datas

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='UTF-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)

        return new_urls, new_data
