#coding:UTF-8
'''
Created on 2016年1月5日

@author: hanqingsong
'''
import urllib2
from compiler.ast import Node


class HtmlDownloader(object):
    
    
    
    def download(self,url):
        if url is None:
            return None
        response = urllib2.urlopen(url)
        print
        if response.getcode() != 200:
            return Node
        return response.read()
        
    
    
    
    



