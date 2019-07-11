#网页图片爬取，并保存到当前程序的img文件夹中，img文件夹需要自己创建

from requests_html import HTMLSession
import requests
import re
import time
import ssl
ssl._create_default_https_context=ssl._create_unverified_context


session=HTMLSession()   #建立会话

url='https://www.cnxiangyan.com/'      #网页地址
#page=request.urlopen(url)  #打开网页   

# htmlcode=page.read()   #读取页面源码
# print(htmlcode)
#超时重试  3次
def gethtml(url):
    i=0
    while i<3:
        try:
            r=session.get(url,timeout=5)  #请求时间5s
            return r
        except:            
            i+=1
            print('重新连接'+str(i))      # i 是数字，不能与字符串进行运算，需要使用str()转换成字符串 

r=gethtml(url)  
# print(r.html.html)
sel='#brands > div.tab-bd > div.brands-content.hot-dzy > ul > li > a > img'
#img_list=r.html.find(sel,first=True) #数组中的第一个元素  相当于 r.html.find(sel)[0]
#print(img_list.attrs['data-original'])  #attrs获取属性值

#解析图片列表
def get_html_img_list(img_url):
    img_lists=[]
    try:
        img_list_arr=r.html.find(sel)
        for img in img_list_arr:
            img_url_0=img.attrs['src']  #attrs获取属性值
            img_lists.append(img_url_0) #图片列表，方便以后使用，比如需要存储图片地址
            res=gethtml(img_url_0) #请求图片地址，二进制
            print(img_url_0)
            t = int(round(time.time() * 1000))  # 毫秒级时间戳，用来给图片命名
            f=open('./img/%d.jpg' % t,'ab')  #存储图片位置和写入方式
            f.write(res.content)       #写入文件
            f.close()   #关闭
        return img_lists    #返回图片列表
    except:
            return None

get_html_img_list(sel)
