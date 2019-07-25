import pymysql
import re

#数据库读取
def db_sel(sql):
    try:
        # dbname='aiyack_cn'
        # 打开数据库连接
        db = pymysql.connect("192.168.1.209","jtcm","qqqAAA0130",'snsnb_com',charset="utf8")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # 使用 execute()  方法执行 SQL 查询 
        cursor.execute(sql) 

        # 获取所有记录列表
        results = cursor.fetchall()
        return results
        
    except Exception:
        # 发生错误时回滚
        db.rollback() 
    db.close() #连接施放
    
    
    

#数据库更新
def db_up(sql):
    try:
        # dbname='aiyack_cn'
        # 打开数据库连接
        db = pymysql.connect("192.168.1.209","jtcm","qqqAAA0130",'snsnb_com',charset="utf8")
        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # 使用 execute()  方法执行 SQL 查询 
        cursor.execute(sql)  #查询栏目名称和栏目路径

        # 获取所有记录列表
        db.commit()  
        db.close() #连接施放
    except Exception:
        # 发生错误时回滚
        db.rollback() 
    


total_number_of_articles="SELECT COUNT(*) from v9_category"
num=db_sel(total_number_of_articles)[0][0] #总条数

print('运行中...')
n=1
while n<num:
    sql_single="SELECT catid,catname,image,description FROM v9_category limit {},1".format(n) #单条
    single=db_sel(sql_single)[0]
    catid=single[0]
    image=single[2]
    description=single[3]
    # print(single)
    v9_category_7_25="SELECT catid,catname,image,description FROM v9_category_7_25 where catid={}".format(catid)
    v9_category_7_25_single=db_sel(v9_category_7_25)[0]
    v9_category_7_25_image=v9_category_7_25_single[2]
    v9_category_7_25_description=v9_category_7_25_single[3]
    # print(v9_category_7_25_single)

    if len(image)<1:    
        sqlupdate_image="update `v9_category` set `image`='{}' where `catid`={}".format(v9_category_7_25_image,catid)  
        db_up(sqlupdate_image)

    if len(description)<1:
        sqlupdate_description="update `v9_category` set `description`='{}' where `catid`={}".format(v9_category_7_25_description,catid) 
        db_up(sqlupdate_description)
    n=n+1

print('完成')