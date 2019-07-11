
import pymysql
import re

db = pymysql.connect("192.168.1.209","jtcm","qqqAAA0130",'ceshi02_com',charset="utf8")
cursor = db.cursor()
try:
    
# 使用 cursor() 方法创建一个游标对象 cursor
    

    # 使用 execute()  方法执行 SQL 查询 
    cursor.execute("SELECT content FROM v9_news_data WHERE id=32309")  #查询栏目名称和栏目路径
    results = cursor.fetchall()
    pattern = re.compile(r'<img *[www\.zhihuige\.cn|cimg\.chinawolong\.com]*.*?>')
    out=re.sub(pattern," ",results[0][0])
    # f=open('1.txt','a',encoding='utf-8')
    # f.write(results[0][0])
    # f.close()
    # f1=open('2.txt','a',encoding='utf-8')
    # f1.write(out)
    # f1.close()
    try:
        sqlupdate="update `v9_news_data` set `content`='{}' where `id`=32309".format(out)             
        
        cursor.execute(sqlupdate)
        db.commit()
    except Exception as e:
        # 发生错误时回滚
        print(e)
        db.rollback() 

    # print(out)
except Exception as e:
    # 发生错误时回滚
    print(e)
    db.rollback() 
    # if results: 
    #     str_txt=results[0][1]
