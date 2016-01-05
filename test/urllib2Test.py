#coding:utf-8
import urllib
import urllib2
import cookielib

print 'urllib2'

url =r'http://www.baidu.com/s'
values = {'wd':'北京'}
data = urllib.urlencode(values)
print data
url2=url + '?' +data

#第一种方法 url参数
print '第一种方法'
response  = urllib2.urlopen(url2)
code = response.getcode()
content = response.read()
#输入错
print code
print len(content)


#第二种方法 requet参数
print '第二种方法'
request = urllib2.Request(url)
request.add_header("user-agent","Mozilla/5.0")
response2 = urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())

print '第三种方法 ：cookie处理'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener);
response3 = urllib2.urlopen(url)
print response3.getcode()
print len(response3.read())
print cj

