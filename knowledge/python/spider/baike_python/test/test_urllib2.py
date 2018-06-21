# -*- coding: utf-8 -*-
import urllib2, cookielib, sys

url = "http://baike.baidu.com/view/21087.htm"

print '第一种方法'
response1 = urllib2.urlopen(url)
content = response1.read();
type = sys.getfilesystemencoding()
print content.decode("UTF-8").encode(type)

#print '第二种方法'
request = urllib2.Request(url)
request.add_header('user-agent', 'Mozilla/5.0')
response2 = urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())

#print '第三种方法'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print response3.getcode()
print cj
print len(response3.read())