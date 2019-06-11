# 批量替换网站图片

import pymysql

# 网站数据库名称列表
#dbnamelist='C:/Users/Administrator/Desktop/dbname.txt'  #路径
#数据库名 网站域名 图片文件夹
line_db_list=[["db_huluwan_com","www.huluwan.com","huluwan_com"],["db_szjcedu_com","www.szjcedu.com","szjcedu_com"],["db_nknzy_com","www.nknzy.com","nknzy_com"],["db_whfisc_com","www.whfisc.com","whfisc_com"],["db_soushu_com","www.sou-shu.com","soushu_com"],["db_xm120_net","www.xm120.net","xm120_net"],["db_sxjrskj_cn","www.sxjrskj.cn","sxjrskj_cn"],["db_dalianhaifu_com","www.dalianhaifu.com","dalianhaifu_com"],["db_qingchun18_com","www.qingchun18.com","qingchun18_com"],["db_chinashengda_com","www.china-shengda.com","chinashengda_com"],["db_xzcit_com","www.xzcit.com","xzcit_com"],["db_hncubbs_com","www.hncubbs.com","hncubbs_com"],["db_tung1_com","tung-1.com","tung1_com"],["db_jlzhongde_com","jlzhongde.com","jlzhongde_com"],["db_guohua17_com","www.guohua17.com","guohua17_com"],["db_qinlaoren_cn","www.qinlaoren.cn","qinlaoren_cn"],["db_sjzzmxsls_cn","www.sjzzmxsls.cn","sjzzmxsls_cn"],["db_haikourcw_cn","www.haikourcw.cn","haikourcw_cn"],["db_junmadaoju_cn","www.junmadaoju.cn","junmadaoju_cn"]]
# for line_db in open(dbnamelist):
#     line_db_list.append(line_db.strip('\n'))

for dbrow in line_db_list:
    dbname=dbrow[0]  #数据库名
    dburl=dbrow[1]  #域名
    dbfilme=dbrow[2]  #文件夹名
    wwwtxt='www.'
    result=wwwtxt in dburl
    if result:
        url=dburl.replace('www.','')  #带www去掉
    else:
        url=dburl   #不带www不变
    try:
        # dbname='aiyack_cn'
        # 打开数据库连接
        db = pymysql.connect("127.0.0.1","root","root",dbname,charset="GBK")

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # 使用 execute()  方法执行 SQL 查询 
        sql1="update dede_archives SET litpic = REPLACE( litpic, '"+dburl+"/uploadfile/', 'img."+url+"/"+dbfilme+"/allimg/' ) where litpic like '%/uploadfile/%';"
        sql2="update dede_addonarticle SET body = REPLACE( body, '"+dburl+"/uploadfile/', 'img."+url+"/"+dbfilme+"/allimg/' ) where body like '%/uploadfile/%';"
        sql3="update dede_uploads SET url = REPLACE( url, '"+dburl+"/uploadfile/', 'img."+url+"/"+dbfilme+"/allimg/' ) where url like '%/uploadfile/%';"

        sql4="update dede_archives SET litpic = REPLACE( litpic, '"+dburl+"/uploads/', 'img."+url+"/"+dbfilme+"/' ) where litpic like '%/uploads/%';"
        sql5="update dede_addonarticle SET body = REPLACE( body, '"+dburl+"/uploads/', 'img."+url+"/"+dbfilme+"/' ) where body like '%/uploads/%';"
        sql6="update dede_uploads SET url = REPLACE( url, '"+dburl+"/uploads/', 'img."+url+"/"+dbfilme+"/' ) where url like '%/uploads/%';"
        try:
            cursor.execute(sql1)
            cursor.execute(sql2)   
            cursor.execute(sql3)   
            cursor.execute(sql4)   
            cursor.execute(sql5)   
            cursor.execute(sql6)       
            
            # 提交到数据库执行
            db.commit()
        except Exception as e:
            # 发生错误时回滚
            db.rollback()
        else:
            print('ok')
            f=open("C:/Users/Administrator/Desktop/"+'img替换.txt','a',encoding='utf-8') #文件保存到桌面db文件夹中
            f.write(dburl+'\n')
            f.close()       
        
        db.close()
    except:
        pass
