from requests_html import HTMLSession       #安装依赖包pip install requests_html 并引入，我们需要的是requests_html包中的HTMLSession功能
session=HTMLSession()   #建立会话
url = 'https://www.jianshu.com/p/85f4624485b9'  #要爬取的页面


#r=session.get(url,timeout=1)  #使用get方法获取页面内容,请求超时1s

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

#print(r.html.text)  #输出html中的文字部分
#print(r.html.links)     #输出html中的所有链接，返回的链接包含相对链接
#print(r.html.absolute_links)    #输出绝对地e址

#===================================
#sel='body > div.note > div.post > div.article > div.show-content > div > p:nth-child(4) > a'    #要去的元素路径规则
#results=r.html.find(sel)
#print(results[0].text)
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

sel_title='body > div.note > div.post > div.article > h1'       #文章标题规则
sel_contetn='body > div.note > div.post > div.article > div.show-content > div'     #文章内容规则

#取文章标题或内容   sel 要抓取的元素规则路径  html_and_text 是否保留标签 True  and  false
def get_article(sel,html_and_text):
    article=''
    if html_and_text:
        try:
            article=r.html.find(sel)[0].html
            return article
        except:
            return None
    else:
        try:
            article=r.html.find(sel)[0].text
            return article
        except:
            return None
        

print(get_article(sel_title,False))
print(get_article(sel_contetn,True))

