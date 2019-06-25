#批量获取数据库中的网站域名地址，友链，并存放到对应的文件中
#网站域名与友链存放到同一个文件中，并将数据库名与网站域名存放到另一个文件中
import pymysql
import os

db_list=["a108","a109","a110","a111","a112","a113","a114","a115","a116","a117","a118","a119","a120","a121","a122","a123","a124","a125","a126","a127","a128","a129","a130","a131","a132","a133","a134","a135","a136","a137","a138","a139","a140","a141","a142","a143","a144","a145","a146","a147","a148","a149","a150","a151","a152","a153","a154","a155","a156","a157","a158","a159","a160","a161","a750","s522","s523","s524","s525","s526","s527","s528","s529","s530","s531","s532","s533","s534","s535","s536","s537","s538","s539","s540","s541","s542","s543","s544","s545","s546","s547","s548","s549","s550","s551","s552","s553","s554","s555","s556","s557","s558","s559","s560","s561","s562","s563","s564","s565","s566","s567","s568","s569","s570","s571","s572","s573","s574","s575","s576","s577","s578","s579","s580","s581","s582","s583","s584","s585","s586","s587","s588","s589","s590","s591","s592","s593","s594","s595","s596","s597","s598","s599","s600","s601","s602","s603","s604","s605","s606","s607","s608","s609","s610","s611","s612","s613","s614","s615","s616","s617","s618","s619","s620","s621","s622","s623","s624","s625","s626","s627","s628","s629","s630","s631","s632","s633","s634","s635","s636","s637","s638","s639","s640","s641","s642","s643","s644","s645","s646","s647","s648","s649","s650","s651","s652","s653","s654","s655","s656","s657","s658","s659","s660","s661","s662","s663","s664","s665","s666","s667","s668","s669","s670","s671","s672","s673","s674","s675","s676","s677","s678","s679","s680","s681","s682","s683","s684","s685","s686"]

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