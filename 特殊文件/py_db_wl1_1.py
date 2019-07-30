#从文件夹的每个文件中取20条数据，并保存到指定文件中
import shutil
import os
import pymysql
import re
import random

#正则 zstr:正则 s:替换成什么内容  stxt：需要替换的内容
def zz(zstr,s,stxt):
    strinfo=re.compile(zstr) #正则匹配最后一个斜杠后的内容
    url_q=strinfo.sub(s,stxt)
    return url_q

dirname="C:/Users/Administrator/Desktop/s" #读取目录
myfileurl='C:/Users/Administrator/Desktop/s1/1.txt'  #保存路径

files_list=[]
for root,dirs,files in os.walk(dirname):
    #print(files)    #当前目录下的文件名列表
    files_list=files
    


for file_name in files_list:
    file_name=dirname+'/'+file_name
    myfile=open(file_name)
    lines=len(myfile.readlines()) #文件总行数
    myfile.close()
    #print(file_name) 
    i=1
    while i<=20:
        n=0
        n=random.randint(1,lines-1) #生成随机数
        print(file_name,n)
        f=open(file_name)
        line=f.readlines()
        first_line=line[int(n)].strip('\n')
        first_line=zz('http|https','',first_line)
        first_line="http"+first_line
        f1=open(myfileurl,'a',encoding='utf-8')
        f1.write(first_line+'\n')
        f1.close()

        f.close()
        i+=1