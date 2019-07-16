
import pymysql
import re

db = pymysql.connect("192.168.1.209","jtcm","qqqAAA0130",'ceshi02_com',charset="utf8")
cursor = db.cursor()

id_arr=["32292","32299","32252","32306","32270","32272","32273","32275","32308","32407","32408","32429","32432","32444","32445","32450","32457","32462","32487","32490","32501","32506","32508","32509","32530","32431","32438","32442","32447","32495","32497","32507","32513","32520","32511","37710","37976","38229","37497","37541","37975","38212","38221","38230","38503","38506","37492","37584","37963","37978","37991","37603","38320","37701","37709","38455","38504","37936","37952","38950","38460","38499","38941","38948","38952","38957","38986","39189","49482","49489","49491","49500","49502","43656","45840","45867","49492","49494","49499","49501","43937","49527","40142","41217","49488","49495","49498","45726","49503","49504","49524","49536","41011","38953","38960","55775","43944","38992","46680","50753","51081","41364","39060","41176","51086","39341","43942","49486","49490","49497","49528","49537","49540","55948","55773"]
for id in id_arr:
    try:
        
    # 使用 cursor() 方法创建一个游标对象 cursor
        

        # 使用 execute()  方法执行 SQL 查询 
        cursor.execute("SELECT content FROM v9_news_data WHERE id={}".format(id))  #查询栏目名称和栏目路径
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
            sqlupdate="update `v9_news_data` set `content`='{}' where `id`={}".format(out,id)             
            
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
