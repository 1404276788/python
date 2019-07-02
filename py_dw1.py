#爬取大马页面中的所有数据库中友链
#coding:utf-8
from requests_html import HTMLSession
import requests, urllib
import os
import re


session = HTMLSession()
url_h='http://www.jhchaoshengbo.com/plus/_btn.php?eanver=mysql_msg&db='

headers={
    "cookie":"envlpass=350bfcb1e3cfb28ddff48ce525d4f139; serveru=www.jhchaoshengbo.com%2Fplus%2F_btn.php; serverp=DD; m_eanverhost=localhost; m_eanverport=3306; m_eanveruser=shuaishuai; m_eanverpass=123456; PHPSESSID=16sb0p9ejgjv0dehp8bg66dj34; DedeUserID=1; DedeUserID__ckMd5=ba8059fc127a1451; DedeLoginTime=1562034805; DedeLoginTime__ckMd5=bc46f2db6a335449; ENV_GOBACK_URL=%2Fadmindede%2Fmedia_main.php%3Fdopost%3Dfilemanager"
}

def gethtml(url):
    i=0
    while i<3:
        try:
            r=session.get(url,headers=headers,timeout=5)  #请求时间5s
            return r
        except:            
            i+=1
            print('重新连接'+str(i))      # i 是数字，不能与字符串进行运算，需要使用str()转换成字符串 
    #最终请求失败返回并记录

db_list=["information_schema","a0032","a043","a1","a10","a11","a12","a13","a14","a15","a16","a17","a18","a19","a2","a20","a21","a22","a23","a24","a25","a26","a27","a28","a29","a3","a30","a31","#mysql50#a32 - ","a33","a34","a35","a36","a37","a38","a39","a4","a40","a41","a42","a43","a44","a45","a46","a47","a48","a49","a5","a50","a51","a52","a53","a54","a55","a56","a57","a58","a59","a6","a60","a61","a62","a63","a7","a8","a9","mysql","performance_schema","s1000","s1001","s1002","s826","s827","s828","s829","s830","s831","s832","s833","s834","s835","s836","s837","s838","s839","s840","s841","s842","s843","s844","s845","s846","s847","s848","s849","s850","s851","s852","s853","s854","s855","s856","s857","s858","s859","s860","s861","s862","s863","s864","s865","s866","s867","s868","s869","s870","s871","s872","s873","s874","s875","s876","s877","s878","s879","s880","s881","s882","s883","s884","s885","s886","s887","s888","s889","s890","s891","s892","s893","s894","s895","s896","s897","s898","s899","s900","s901","s902","s903","s904","s905","s906","s907","s908","s909","s910","s911","s912","s913","s914","s915","s916","s917","s918","s919","s920","s921","s922","s923","s924","s925","s926","s927","s928","s929","s930","s931","s932","s933","s934","s935","s936","s937","s938","s939","s940","s941","s942","s943","s944","s945","s946","s947","s948","s949","s950","s951","s952","s953","s954","s955","s956","s957","s958","s959","s960","s961","s962","s963","s964","s965","s966","s967","s968","s969","s970","s971","s972","s973","s974","s975","s976","s977","s978","s979","s980","s981","s982","s983","s984","s985","s986","s987","s988","s989","s990","s991","s992","s993","s994","s995","s996","s997","s998","s999","shuaishuai"]


for dbname in db_list:
    url_h=url_h+"{}".format(dbname)
    sel='table > tr > td:nth-child(1) > a'
    r=gethtml(url_h)
    s=r.html.find(sel)
    for val in s:
        #print(val.text)
        v=val.text
        m=re.search("_flink$",v)
        if m:
            m=re.search("member_flink$",v)
            if m:   #过滤member_flink
                pass
            else:
                print(dbname+' '+v)
                sel_n='div:nth-child(7)'
                i=1
                url_flink=url_h+'{}&table={}&p={}&charset='.format(dbname,v,i)
                #获取页数
                r2=gethtml(url_flink)
                s2=r2.html.find(sel_n)
                s2=s2[0].text
                n=re.findall(r'\/\d',s2)[0][1:] #取页数
                #print(n)
                n=int(n)
                #获取数据
                while i<=n:                
                    sel='table > tr > td:nth-child(4)'    
                    url_flink=url_h+'{}&table={}&p={}&charset='.format(dbname,v,i)            
                    r1=gethtml(url_flink)
                    s1=r1.html.find(sel)
                    for val in s1:
                        if (val.text!='url'):
                            # print(dbname)
                            f=open('网址.txt','a',encoding='utf-8')
                            f.write(val.text+'\n')
                            f.close()
                    i=i+1
                
                
                











        




