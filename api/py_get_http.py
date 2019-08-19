#url请求功能
from requests_html import HTMLSession
import re
import time
import ssl

ssl._create_default_https_context=ssl._create_unverified_context

session=HTMLSession()   #建立会话


def gethtml_30(url):
    i=0
    while i<3:
        try:
            r=session.get(url,timeout=30)  #请求时间
            return r
        except:            
            i+=1
            print('重新连接'+str(i))      # i 是数字，不能与字符串进行运算，需要使用str()转换成字符串 

def gethtml_5(url):
    i=0
    while i<3:
        try:
            r=session.get(url,timeout=5)  #请求时间
            return r
        except:            
            i+=1
            print('重新连接'+str(i))      # i 是数字，不能与字符串进行运算，需要使用str()转换成字符串 

def posthtml_30(url,postdata):
    i=0
    while i<3:
        try:
            r=session.post(url,data=postdata,timeout=30)  #请求时间
            return r
        except:            
            i+=1
            print('重新连接'+str(i))      # i 是数字，不能与字符串进行运算，需要使用str()转换成字符串 

def posthtml_5(url,postdata):
    i=0
    while i<3:
        try:
            r=session.post(url,data=postdata,timeout=5)  #请求时间
            return r
        except:            
            i+=1
            print('重新连接'+str(i))      # i 是数字，不能与字符串进行运算，需要使用str()转换成字符串 