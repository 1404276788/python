import pymysql


#数据库读取
def db_rand_wl(dbname,sql):
    try:
        # dbname='aiyack_cn'
        # 打开数据库连接
        db = pymysql.connect("rm-bp1915vx2p313r181o.mysql.rds.aliyuncs.com","dz_snsnb_com","qqqAAA0130",dbname,charset="utf8")

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # 使用 execute()  方法执行 SQL 查询 
        cursor.execute(sql)  #查询栏目名称和栏目路径

        # 获取所有记录列表
        results = cursor.fetchall()
        # print(results)
        return results
        
        db.close() #连接施放
    except Exception as e:
        # 发生错误时回滚
        db.rollback() 



dbnamelist=['dz_snsnb_com']
#'portal_article_content','portal_article_count','portal_article_related','portal_article_title'
#'portal_attachment','portal_category','portal_rsscache'
dbtablelist=['portal_article_title']

aid='430'
for dbname in dbnamelist:
    for dbtable in dbtablelist:
        # sql='select * from {}.ivf_{} where aid={}'.format(dbname,dbtable,aid)
        sql='select aid,catid from {}.ivf_{}'.format(dbname,dbtable)
        # print(sql)
        res=db_rand_wl(dbname,sql)
        f=open('snsnb\{}.txt'.format(dbtable),'a',encoding='utf-8')
        for list_m in res:        
        #https://www.snsnb.com/post-148380-1.html
            url='https://www.snsnb.com/post-{}-1.html'.format(str(list_m[0]))
            lanmu='cid:'+str(list_m[1])
            # print('https://www.snsnb.com/post-{}-1.html'.format(str(list_m[0])))     
            # print('cid:'+str(list_m[1]))   
            f.write(url+" "+lanmu+'\n')  
        # for val in res:  
            # f.write(str(val)+'\n')              
            # print(val)
        # f.write('------------------------------------------------------------------------------------------\n')   
        f.close() 
