#批量获取数据库中的网站域名地址，友链，并存放到对应的文件中
#网站域名与友链存放到同一个文件中，并将数据库名与网站域名存放到另一个文件中
import pymysql
import os

db_list=["a1","a10","a2","a3","a4","a5","a6","a7","a8","a9","a999","k110","k111","k112","k113","k114","k115","k116","k117","k118","k119","k120","k121","k122","k123","k124","k125","k126","k127","k128","k129","k130","k131","k132","k133","k134","k135","k136","k137","k138","k139","k140","k141","k142","k143","k144","k145","k146","k147","k148","k149","k150","k151","k152","k153","k154","k155","k156","k157","k158","k159","k160","k161","k162","k163","k164","k165","k166","k167","k168","k169","k170","k171","k172","k173","k174","k175","k176","k177","k178","k179","k180","k181","k182","k183","k184","k185","k186","k187","k188","k189","k190","k191","k192","k193","k194","k195","k196","k197","k198","k199","k200","k201","k202","k203","k204","k205","k206","k207","k208","k209","k210","k211","k212","k213","k214","k215","k216","k217","k218","k219","k220","k221","k222","k223","k224","k225","k226","k227","k228","k229","k230","k231","k232","k233","k234","k235","k236","k237","k238","k239","k240","k241","k242","k243","k244","k245","k246","k247","k248","k249","k250","k251","k252","k253","k254","k255","k256","k257","k258","k259","k260","k261","k262","k263","k264","k265","k266","k267","k268","k269","k270","k271","k272","k273","k274","k275","k276","k277","k278","k279","k280","k281","k282","k283","k284","k285","k286","k287","k288","k289","k290","k291","k292","k293","k294","k295","k296","k297","k298","k299","k300","k301","k302","k303","k304","k305","k306","k307","k308","k309","k310","k311","k312","k313","k314","k315","k316","k317","k318","k319","k320","k321","k322","k323","k324","k325","k326","k327","k328","k329","k330","k331","k332","k333","k334","k335","k336"]

db_url_list="C:/Users/Administrator/Desktop/db_url_list1.txt" #存放网站域名与友链的文件
db_name_url="C:/Users/Administrator/Desktop/db_name_url1.txt" #存放网站域名与数据库名的文件

for db_name in db_list:
    try:
        # 打开数据库连接
        db = pymysql.connect("127.0.0.1","root","root",db_name,charset="utf8")

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()
        sql='select `value` from dede_sysconfig where varname="cfg_basehost"'
        cursor.execute(sql)  
        results = cursor.fetchall()
        print(db_name)
        if results:
            f0=open(db_url_list,'a',encoding='utf-8') #文件保存到桌面db文件夹中
            f0.write(results[0][0]+'\n')
            f0.close()

        f=open(db_name_url,'a',encoding='utf-8') #文件保存到桌面db文件夹中
        f.write(results[0][0]+"   "+db_name+'\n')
        f.close()

        sql1='select url from dede_flink'
        cursor.execute(sql1)  
        results1 = cursor.fetchall()
        if results1:
            for res in results1:
                # print(res[0])
                f1=open(db_url_list,'a',encoding='utf-8') #文件保存到桌面db文件夹中
                f1.write(res[0]+'\n')
                f1.close()
        
        db.close() #连接施放

    except Exception as e:
        # 发生错误时回滚
        db.rollback()  