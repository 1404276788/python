#网页图片爬取，并保存到当前程序的img文件夹中，img文件夹需要自己创建

from requests_html import HTMLSession
import requests
import re
import time
import ssl
ssl._create_default_https_context=ssl._create_unverified_context


session=HTMLSession()   #建立会话

url='https://www.cnxiangyan.com/'      #网页地址

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
sel='body > div.main > div > div.topbang a'
#sel='#sideMen1 > li:nth-child(1) > a'
sel_arr=r.html.find(sel)
for i in sel_arr:
    url_l=list(i.absolute_links)[0]
    r=gethtml(url_l)
    sel_arr={
        'title':'body > div.main > div.w1220 > div.pleft > div.product > div.show > div.title > h1',#标题
        'type':'body > div.main > div.w1220 > div.pleft > div.product > div.show > div.intro > div.txt > ul > li:nth-child(1) > span',#类型
        'tar_amount':'body > div.main > div.w1220 > div.pleft > div.product > div.show > div.intro > div.txt > ul > li:nth-child(2) > span',#焦油量
        'fgnc':'body > div.main > div.w1220 > div.pleft > div.product > div.show > div.intro > div.txt > ul > li:nth-child(3) > span',#烟气烟碱量
        'aocm':'body > div.main > div.w1220 > div.pleft > div.product > div.show > div.intro > div.txt > ul > li:nth-child(4) > span',#一氧化碳量
        'smoke_len':'body > div.main > div.w1220 > div.pleft > div.product > div.show > div.intro > div.txt > ul > li:nth-child(5) > span',#一氧化碳量
        'filter_len':'body > div.main > div.w1220 > div.pleft > div.product > div.show > div.intro > div.txt > ul > li:nth-child(6) > span',#烟长
        'package_style':'body > div.main > div.w1220 > div.pleft > div.product > div.show > div.intro > div.txt > ul > li:nth-child(7) > span',#包装形式
        'single_box_count':'body > div.main > div.w1220 > div.pleft > div.product > div.show > div.intro > div.txt > ul > li:nth-child(8) > span',#单盒(包)支数
        'main_color':'body > div.main > div.w1220 > div.pleft > div.product > div.show > div.intro > div.txt > ul > li:nth-child(9) > span',#包装主色调
        'packing_subtone':'body > div.main > div.w1220 > div.pleft > div.product > div.show > div.intro > div.txt > ul > li:nth-child(10) > span',#包装副色调
        'sales_form':'body > div.main > div.w1220 > div.pleft > div.product > div.show > div.intro > div.txt > ul > li:nth-child(11) > span',#销售形式
        'product_status':'body > div.main > div.w1220 > div.pleft > div.product > div.show > div.intro > div.txt > ul > li:nth-child(12) > span',#产品状态
        'single_box_price':'body > div.main > div.w1220 > div.pleft > div.product > div.show > div.intro > div.txt > ul > li:nth-child(13) > span',#单盒参考价
        'box_reference_price':'body > div.main > div.w1220 > div.pleft > div.product > div.show > div.intro > div.txt > ul > li:nth-child(14) > span',#条盒参考价
        'recommended':'body > div.main > div.w1220 > div.pleft > div.product > div.show > div.intro > div.txt > ul > li:nth-child(15) > span',#推荐指数
        'num_people':'#score_num',#评分人数
        'credibility':'#score_reliability',#可信度
        'taste':'#kwfs > span',#口味        
        'exterior':'#wgfs > span',#外观
        'value_for_money':'#xjfs > span' #性价比
    }

    title=r.html.find(sel_arr['title'])[0].text
    types=r.html.find(sel_arr['type'])[0].text
    tar_amount=r.html.find(sel_arr['tar_amount'])[0].text
    fgnc=r.html.find(sel_arr['fgnc'])[0].text
    aocm=r.html.find(sel_arr['aocm'])[0].text
    smoke_len=r.html.find(sel_arr['smoke_len'])[0].text
    filter_len=r.html.find(sel_arr['filter_len'])[0].text
    package_style=r.html.find(sel_arr['package_style'])[0].text
    single_box_count=r.html.find(sel_arr['single_box_count'])[0].text
    main_color=r.html.find(sel_arr['main_color'])[0].text
    packing_subtone=r.html.find(sel_arr['packing_subtone'])[0].text
    sales_form=r.html.find(sel_arr['sales_form'])[0].text
    product_status=r.html.find(sel_arr['product_status'])[0].text
    single_box_price=r.html.find(sel_arr['single_box_price'])[0].text
    box_reference_price=r.html.find(sel_arr['box_reference_price'])[0].text
    recommended=r.html.find(sel_arr['recommended'])[0].text
    num_people=r.html.find(sel_arr['num_people'])[0].text
    credibility=r.html.find(sel_arr['credibility'])[0].text
    #taste=r.html.find(sel_arr['taste'])[0].text
    # exterior=r.html.find(sel_arr['exterior'])[0].text
    # value_for_money=r.html.find(sel_arr['value_for_money'])[0].text
    #print(taste)
    tar_amount=tar_amount.replace('mg','')
    fgnc=fgnc.replace('mg','')
    aocm=aocm.replace('mg','')
    smoke_len=smoke_len.replace('mm','')
    filter_len=filter_len.replace('mm','')
    single_box_price=single_box_price.replace('￥','')
    box_reference_price=box_reference_price.replace('￥','')
    f=open('C:/Users/Administrator/Desktop/yancao/'+title+'.txt','a',encoding='utf-8')
    f.write(title+'\n'+types+'\n'+tar_amount+'\n'+fgnc+'\n'+aocm+'\n'+smoke_len+'\n'+filter_len+'\n'+package_style+'\n'+single_box_count+'\n'+main_color+'\n'+packing_subtone+'\n'+sales_form+'\n'+product_status+'\n'+single_box_price+'\n'+box_reference_price+'\n'+recommended+'\n'+num_people+'\n'+credibility+'\n')
    f.close()
    



