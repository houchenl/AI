import urllib2

url = 'http://baike.baidu.com/view/21087.htm'

response = urllib2.urlopen(url)

if response.getcode() != 200:
	print None
else:
	cont = response.read()
	print cont
