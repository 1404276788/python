# mongo 设置唯一字段去重
import os
from pymongo import MongoClient
conn = MongoClient('192.168.1.118', 27017)
db_mongo = conn.mydb  # 连接mydb数据库，没有则自动创建
my_set = db_mongo.shell_data  # 使用 toutiao_key 集合，没有则自动创建
my_set.create_index([("url", 1)], unique=True)  # 设置唯一字段 key 去重



fo1 = open("D:/mgdb.txt",'r')
for line in fo1:
    line = line.strip('\n')
    try:
        my_set.insert({"url": line, 'status':1})
    except Exception as e:
        pass
    else:
        fo3 = open("D:/sql3.txt", 'a')
        fo3.write(line + "\n")
        fo3.close()
fo1.close()