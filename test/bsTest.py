#coding:utf-8
'''
Created on 2016年1月5日

@author: hanqingsong
'''
import re
import urllib
import urllib2

from bs4 import BeautifulSoup
import bs4


print 'bsTest'
#print bs4

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

soup = BeautifulSoup(content)
#输入错
print code
print len(content)
#print soup.prettify()
#print soup.title   #<title>北京_百度搜索</title>
all_a = soup.find_all('a')
for a in all_a:    
    if a.get("href") != None and a.string !=None:
        print a.get("href") #print a["href"]        
        #print a
        print a.string
print '正则匹配'
link_node = soup.find('a',href=re.compile(r"wenku"))
print link_node
print soup.title.name
print soup.title.string
print 

