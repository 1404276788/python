import pymysql
import re
import random
import string

#数据库读取
def db_rand_wl():
    try:
        # dbname='aiyack_cn'
        # 打开数据库连接
        db = pymysql.connect("192.168.1.209","jtcm","qqqAAA0130",'ali',charset="utf8")

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # 使用 execute()  方法执行 SQL 查询 
        cursor.execute("SELECT url FROM rand_wl ORDER BY RAND() LIMIT 10")  #查询栏目名称和栏目路径

        # 获取所有记录列表
        results = cursor.fetchall()
        return results
        
        db.close() #连接施放
    except Exception as e:
        # 发生错误时回滚
        db.rollback() 


#数据处理
def db_htmls():
    list_arr=db_rand_wl()
    s=''
    for v in list_arr:
        a=''.join(random.sample(string.ascii_letters + string.digits, 10)) #ascii_letters 字母 digits 数字 随机生成10位
        s=s+"<a href='{}'></a>\n<a href='tags_class.php?{}.html'></a>\n".format(v[0],a)

    ss='<html lang="zh-CN" class="no-js">\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n'
    ss=ss+'<div class="rel_news">\n<div class="itemlist">\n'+s+'</div>\n</head>\n</html><html'
    return ss
