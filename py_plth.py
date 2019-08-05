# dede文章内容批量替换
import pymysql
import re
import html


line_db_list=["ali"]      #数据库列表
prefix='jtcm'   #表前缀

for dbrow in line_db_list:
    dbname=dbrow
    try:
        # 打开数据库连接
        db = pymysql.connect("192.168.1.209","jtcm","qqqAAA0130",dbname,charset="utf8")

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        numsql="SELECT COUNT(*) FROM {}_addonarticle".format(prefix)
        cursor.execute(numsql)
        num = cursor.fetchall() #获取表中数据的总条数
        
        
        i=0 #默认开始

        for i in range(num[0][0]):  
            # print(i)      
            # 使用 execute()  方法执行 SQL 查询 
            # 使用 cursor() 方法创建一个游标对象 cursor           
            
            sql="SELECT aid,body FROM {}_addonarticle LIMIT {},1".format(prefix,i)
            # print(sql)
            try:
                cursor.execute(sql)
                # 获取所有记录列表
                results = cursor.fetchall()
                if results:            
                    # print(results[0][0])
                    str_txt=results[0][1]
                    aid=results[0][0]
                    
                    pattern = re.compile(r'http:\/\/.*?\/sitemap\/')
                    out=re.sub(pattern,"",str_txt)
                    try:
                        sqlupdate="update `{}_addonarticle` set `body`='{}' where `aid`={}".format(prefix,out,aid)             
                        
                        cursor.execute(sqlupdate)
                        db.commit()
                    except Exception as e:
                        # 发生错误时回滚
                        print(e)
                        db.rollback() 
                    else:
                        # db.close()
                        out=''
                        i=i+1 
                else:
                    break
            except Exception as e:
                # 发生错误时回滚
                db.rollback()    
    except:
        pass
    db.close()
