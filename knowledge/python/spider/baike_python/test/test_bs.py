# coding:utf8
from bs4 import BeautifulSoup
import re
import urllib2

url = 'http://baike.baidu.com/view/21087.htm'

response = urllib2.urlopen(url)

cont = response.read()
print cont

