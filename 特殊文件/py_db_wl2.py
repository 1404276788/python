#功能
#将寄生虫路径写入数据库
#动态寄生虫每个路径后面随机拼接字符串，生成20个不同的路径，然后写入到数据库中的rand_wl表中
import shutil
import os
import pymysql
import re
import random
import string

#正则 zstr:正则 s:替换成什么内容  stxt：需要替换的内容
def zz(zstr,s,stxt):
    strinfo=re.compile(zstr) #正则匹配最后一个斜杠后的内容
    url_q=strinfo.sub(s,stxt)
    return url_q

file_name="C:/Users/Administrator/Desktop/s1/1.txt"

for line in open(file_name,encoding='utf-8'):    
    if line:
        i=1
        while i<=20:
            a=''.join(random.sample(string.ascii_letters + string.digits, 10)) #ascii_letters 字母 digits 数字 随机生成10位
            s=line.strip('\n')+'?'+a+".html"  #line.strip('\n') 去除换行
            # f=open('C:/Users/Administrator/Desktop/s1/2.txt','a',encoding='utf-8')
            # f.write(s+'\n')
            # f.close()
            i+=1
            db = pymysql.connect("127.0.0.1","root","root",'wl',charset="utf8")
            # 使用 cursor() 方法创建一个游标对象 cursor
            cursor = db.cursor()            
            sql='INSERT INTO wl_url (url) VALUES ("{}")'.format(s)
            try:
                cursor.execute(sql)
                # print(1)
                db.commit()
                
            except Exception as e:
                # 发生错误时回滚
                db.rollback()
            db.close()
