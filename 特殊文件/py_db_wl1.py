#功能
#文件夹中的所有文本文件中的数据批量写入数据库
#将寄生虫路径批量写入数据库
import shutil
import os
import pymysql
import re


#正则 zstr:正则 s:替换成什么内容  stxt：需要替换的内容
def zz(zstr,s,stxt):
    strinfo=re.compile(zstr) #正则匹配最后一个斜杠后的内容
    url_q=strinfo.sub(s,stxt)
    return url_q


dirname="C:/Users/Administrator/Desktop/s1"
files_list=[]
for root,dirs,files in os.walk(dirname):
    #print(files)    #当前目录下的文件名列表
    files_list=files

for file_name in files_list:
    file_name=dirname+'/'+file_name
    for line in open(file_name,encoding='utf-8'):
        if line:            
            line=zz('http|https','',line)
            line="http"+line
            #print(line,end='')           
            db = pymysql.connect("127.0.0.1","root","root",'wl',charset="utf8")
            # 使用 cursor() 方法创建一个游标对象 cursor
            cursor = db.cursor()            
            sql='INSERT INTO wl_url (url) VALUES ("{}")'.format(line)
            # print(sql)
            try:
                cursor.execute(sql)
                # print(1)
                db.commit()
                
            except Exception as e:
                # 发生错误时回滚
                db.rollback()
        db.close()


