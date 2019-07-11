import pandas as pd #数据框工具，将列表变成数据框，可实现转换成表输出
from requests_html import HTMLSession       #安装依赖包pip install requests_html 并引入，我们需要的是requests_html包中的HTMLSession功能
session=HTMLSession()   #建立会话
url = 'http://127.0.0.1:8080/index.html'  #要爬取的页面

r=session.get(url)  #使用get方法获取页面内容
#print(r.html.text)  #输出html中的文字部分
#print(r.html.links)     #输出html中的所有链接，返回的链接包含相对链接
#print(r.html.absolute_links)    #输出绝对地e址
results=r.html.find('a')
f=open('url_list1.txt','a',encoding='utf-8')
for v in results:
        # print(v.attrs['href'])
        # for url_s in r.html.absolute_links:
        result='http' in v.attrs['href']
        if result:
                f.write(v.attrs['href']+'【'+v.text+'】'+'\n')
f.close()


