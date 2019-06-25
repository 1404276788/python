# 内置模块shutil
import shutil
import os

dirname="D:/www/备份文件/新建文件夹"
newname="D:/www/备份文件/a"
files_list=[]
for root,dirs,files in os.walk(dirname):
    #print(files)    #当前目录下的文件名列表
    files_list=files


for file_name in files_list:
    readPath=dirname+"/"+file_name
    writePath=newname+"/"+file_name
    lines_seen=set()
    outfiile=open(writePath,'a+',encoding='utf-8')
    f=open(readPath,'r',encoding='utf-8')
    for line in f:
        if line not in lines_seen:
            outfiile.write(line)
            lines_seen.add(line)



