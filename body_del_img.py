# 删除文章body中的图片
import pymysql
import re
import html


line_db_list=["db_cacker_net","db_177dnf_com","db_mooncolour_com","db_3goldensluxpro_com"]      #数据库列表


for dbrow in line_db_list:
    dbname=dbrow
    try:
        # 打开数据库连接
        db = pymysql.connect("127.0.0.1","root","root",dbname,charset="utf8")

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        numsql="SELECT COUNT(*) FROM dede_addonarticle"
        cursor.execute(numsql)
        num = cursor.fetchall() #获取表中数据的总条数
        
        
        i=0 #默认开始

        for i in range(num[0][0]):  
            # print(i)      
            # 使用 execute()  方法执行 SQL 查询 
            # 使用 cursor() 方法创建一个游标对象 cursor           
            
            sql="SELECT aid,body FROM dede_addonarticle LIMIT {},1".format(i)
            # print(sql)
            try:
                cursor.execute(sql)
                # 获取所有记录列表
                results = cursor.fetchall()
                if results:            
                    # print(results[0][0])
                    str_txt=results[0][1]
                    aid=results[0][0]
                    
                    pattern = re.compile(r'<img .*?>')
                    out=re.sub(pattern," ",str_txt)
                    pattern = re.compile(r'\r\n')  #转义换行
                    out=re.sub(pattern,"<br/>",str_txt) 
                    pattern = re.compile(r'\'')  #转单引号
                    out=re.sub(pattern,"&apos;",str_txt)
                    pattern = re.compile(r'\"') #转双引号
                    out=re.sub(pattern,"&quot;",str_txt)
                    out = str(out) 
                    out=html.escape(out)      #html转义          
                    try:
                        sqlupdate="update `dede_addonarticle` set `body`='{}' where `aid`={}".format(out,aid)             
                        
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
