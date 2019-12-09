# 批量导出phpcms网站的栏目名称和路径
# dbnamelist 数据库名称文件路径地址，一次只能操作一个服务器上的数据库
# db 数据库连接信息

import pymysql

# 网站数据库名称列表
dbnamelist='C:/Users/admin/Desktop/wzurl.txt'  #路径

line_db_list=[]
for line_db in open(dbnamelist):
    line_db_list.append(line_db.strip('\n'))

for dbrow in line_db_list:
    dbname=dbrow
    try:
        # dbname='aiyack_cn'
        # 打开数据库连接
        db = pymysql.connect("192.168.1.216","jtcm","qA0130",dbname,charset="GBK")

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # 使用 execute()  方法执行 SQL 查询 
        cursor.execute("SELECT v9_category.catname,url FROM v9_category")  #查询栏目名称和栏目路径

        # 获取所有记录列表
        results = cursor.fetchall()

        for row in results:
            rowname=row[0]
            rowurl=row[1]    
            f=open("C:/Users/admin/Desktop/db/"+dbname+'.txt','a',encoding='utf-8') #文件保存到桌面db文件夹中
            f.write(rowname+"   "+rowurl+'\n')
            f.close()
        db.close() #连接施放
    except:
        pass
