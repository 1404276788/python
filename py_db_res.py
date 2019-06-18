#批量获取数据库中的网站域名地址，友链，并存放到对应的文件中
#网站域名与友链存放到同一个文件中，并将数据库名与网站域名存放到另一个文件中
import pymysql
import os

db_list=["a1","a10","a100","a101","a102","a103","a104","a105","a106","a107","a11","a12","a13","a14","a15","a16","a17","a18","a19","a2","a20","a21","a22","a23","a24","a25","a26","a27","a28","a29","a3","a30","a31","a32","a33","a34","a35","a36","a37","a38","a39","a4","a40","a41","a42","a43","a44","a45","a46","a47","a48","a49","a5","a50","a51","a52","a53","a54","a55","a56","a57","a58","a59","a6","a60","a61","a62","a63","a64","a65","a66","a67","a68","a69","a7","a70","a71","a72","a73","a74","a75","a76","a77","a78","a79","a8","a80","a81","a82","a83","a84","a85","a86","a87","a88","a89","a9","a90","a91","a92","a93","a94","a95","a96","a97","a98","a99","s1122","s1123","s1124","s1125","s1126","s1127","s1128","s1129","s1130","s1131","s1132","s1133","s1134","s1135","s1136","s1137","s1138","s1139","s1140","s1141","s1142","s1143","s1144","s1145","s1146","s1147","s1148","s1149","s1150","s1151","s1152","s1153","s1154","s1155","s1156","s1157","s1158","s1159","s1160","s1161","s1162","s1163","s1164","s1165","s1166","s1167","s1168","s1169","s1170","s1171","s1172","s1173","s1174","s1175","s1176","s1177","s1178","s1179","s1180","s1181","s1182","s1183","s1184","s1185","s1186","s1187","s1188","s1189","s1190","s1191","s1192","s1193","s1194","s1195","s1196","s1197","s1198","s1199","s1200","s1201","s1202","s1203","s1204","s1205","s1206","s1207","s1208","s1209","s1210","s1211","s1212","s1213","s1214","s1215","s1216","s1217","s1218","s1219","s1220","s1221"]

db_url_list="C:/Users/Administrator\Desktop/db_url_list.txt" #存放网站域名与友链的文件
db_name_url="C:/Users/Administrator\Desktop/db_name_url.txt" #存放网站域名与数据库名的文件

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