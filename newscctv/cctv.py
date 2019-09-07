

import sys
import os
import json

currentUrl = os.path.dirname(__file__)
parentUrl = os.path.abspath(os.path.join(currentUrl, os.pardir))

sys.path.append(parentUrl)
from api.pachong_article import *
url = 'http://news.cctv.com/data/index.json'  # 要爬取的页面

sel_title = '#container > h1'  # 文章标题规则
sel_contetn = '#conter2018'  # 文章内容规则

r = gethtml(url)
news_json=json.loads(r.text)['rollData']
for news in news_json:
    print(news['url'])
r1=gethtml()
