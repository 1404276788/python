# 获取页面状态码
import requests
from urllib import request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://www.cnxiangyan.com/article/15578.html'
# data = request.urlopen('https://www.jk3721.com/html/lsbk/etxg/201707/753466.html').read().decode("gbk")
# r=requests.get(url='https://www.jk3721.com/html/lsbk/etxg/201707/753466.html',timeout=5).html


def gethtml(url):
    i = 0
    while i < 5:
        try:
            # r = session.get(url, timeout=10)  # 请求时间5s
            r = request.urlopen(url).read().decode("gbk")
            return r
        except:
            i += 1
            print('重新连接'+str(i))      # i 是数字，不能与字符串进行运算，需要使用str()转换成字符串


sel_title = 'body > div.main > div > div.pleft > div.m-center-l > h1'  # 文章标题规则


def get_article(sel, html_and_text):
    article = ''
    if html_and_text:
        try:
            article = r.html.find(sel)[0].html
            print(article)
            return article
        except:
            return None
    else:
        try:
            print(article)
            return article
        except:
            return None


r = gethtml(url)


print(get_article(sel_title, True))
