import pandas as pd #数据框工具，将列表变成数据框，可实现转换成表输出
from requests_html import HTMLSession       #安装依赖包pip install requests_html 并引入，我们需要的是requests_html包中的HTMLSession功能
session=HTMLSession()   #建立会话
url = 'https://www.jk3721.com/html/lsbk/etxg/201707/753466.html'  #要爬取的页面

r=session.get(url)  #使用get方法获取页面内容
#print(r.html.text)  #输出html中的文字部分
#print(r.html.links)     #输出html中的所有链接，返回的链接包含相对链接
#print(r.html.absolute_links)    #输出绝对地e址

#===================================
sel='head > title'   #要去的元素路径规则
results=r.html.find(sel)
print(results[0].text)
#print(results[0].absolute_links)    #返回一个集合
#s=list(results[0].absolute_links)     #集合转换成列表
#rint(ls[0])    #打印列表中的第一个元素
#=====改部分功能封装成函数，如下=======

#传入元素规则，返回链接元素的标题和链接
def get_text_link_from_sel(sel):
    mylist=[]
    try:
        results=r.html.find(sel)
        for result in results:
            mytext=result.text
            mylink=list(result.absolute_links)[0]
            mylist.append((mytext,mylink))   #将每一组的标题和链接加到数组中
        return mylist   #返回数组
    except:
        return None

# sel='head > title'
# text_link=get_text_link_from_sel(sel)
#print(text_link)
# df=pd.DataFrame(text_link)  #转换为表
# df.columns=['text','link']  #添加表头
# df.to_csv('output.csv',encoding='gbk',index=False)  #当前目录保存表，格式为gbk

