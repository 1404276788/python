#功能
#动态寄生虫每个路径后面随机拼接字符串，生成20个不同的路径，保存到指定文件中
import shutil
import os
# import pymysql
import re
import random
import string

#正则 zstr:正则 s:替换成什么内容  stxt：需要替换的内容
def zz(zstr,s,stxt):
    strinfo=re.compile(zstr) #正则匹配最后一个斜杠后的内容
    url_q=strinfo.sub(s,stxt)
    return url_q

file_name="abc.txt" #读文件

for line in open(file_name,encoding='utf-8'):    
    if line:
        i=1
        while i<=20:
            #a=''.join(random.sample(string.ascii_letters + string.digits, 10)) #ascii_letters 字母 digits 数字 随机生成10位
            a=''.join(random.sample(string.digits, 10)) #ascii_letters 字母 digits 数字 随机生成10位
            s=line.strip('\n')+'?'+a+".html"  #line.strip('\n') 去除换行
            f=open('1.txt','a',encoding='utf-8') #写文件
            f.write(s+'\n')
            f.close()
            i+=1
            
