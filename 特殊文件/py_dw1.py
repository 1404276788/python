# 爬取大马页面中的所有数据库中友链
# coding:utf-8
from requests_html import HTMLSession
import requests
import urllib
import os
import re


session = HTMLSession()
url_h1 = 'http://www.czjiuli.com/pic/Teams.php?eanver=mysql_msg&db='

headers = {
    "cookie": "envlpass=aafe421b8ad20fe391be17a529c844c2; serveru=www.czjiuli.com%2Fpic%2FTeams.php; serverp=cc11; m_eanverhost=localhost; m_eanverport=3306; m_eanveruser=shuaishuai; m_eanverpass=123456; PHPSESSID=ceje4sa5ds953ng5pjtp9qk4j7; DedeUserID=1; DedeUserID__ckMd5=34adf61cb932ee14; DedeLoginTime=1565772183; DedeLoginTime__ckMd5=c897902093df814c; ENV_GOBACK_URL=%2Fmanager%2Fmedia_main.php%3Fdopost%3Dfilemanager"
}


def gethtml(url):
    i = 0
    while i < 3:
        try:
            r = session.get(url, headers=headers, timeout=5)  # 请求时间5s
            return r
        except:
            i += 1
            print('重新连接'+str(i))      # i 是数字，不能与字符串进行运算，需要使用str()转换成字符串
    # 最终请求失败返回并记录


db_list = ["a0140","a038","a060","a065","a1","a10","a100","a101","a102","a103","a104","a105","a106","a107","a108","a109","a11","a110","a111","a112","a113","a114","a115","a116","a117","a118","a119","a12","a120","a121","a122","a123","a124","a125","a126","a127","a128","a129","a13","a130","a131","a132","a133","a134","a135","a136","a137","a138","a139","a14","a140","a141","a142","a143","a144","a145","a146","a15","a16","a17","a18","a19","a2","a20","a21","a22","a23","a24","a25","a26","a27","a28","a29","a3","a30","a31","a32","a33","a34","a35","a36","a37","a38112","a39","a4","a40","a41","a42","a43","a44","a45","a46","a47","a48","a49","a5","a50","a51","a52","a53","a54","a55","a56","a57","a58","a59","a6","a60","a61","a62","a63","a64","a65","a66","a67","a68","a69","a7","a70","a71","a72","a73","a74","a75","a76","a77","a78","a79","a8","a80","a81","a82","a83","a84","a85","a86","a87","a88","a89","a9","a90","a91","a92","a93","a94","a95","a96","a97","a98","a99","a999","mysql","performance_schema","s687","s688","s689","s690","s691","s692","s693","s694","s695","s696","s697","s698","s699","s700","s701","s702","s703","s704","s705","s706","s707","s708","s709","s710","s711","s712","s713","s714","s715","s716","s717","s718","s719","s720","s721","s722","s723","s724","s725","s726","s727","s728","s729","s730","s731","s732","s733","s734","s735","s736","s737","s738","s739","s740","s741","s742","s743","s744","s745","s746","s747","s748","s749","s750","s751","s752","s753","s754","s755","s756","s757","s758","s759","s760","s761","s762","s763","s764","s765","s766","s767","s768","s769","s770","s771","s772","s773","s774","s775","s776","s777","s778","s779","s780","s781","s782","s783","s784","s785","s786","s787","s788","s789","s790","s791","s792","s793","s794","s795","s796","s797","s798","s799","s800","s801","s802","s803","s804","s805","s806","s807","s808","s809","s810","s811","s812","s813","s814","s815","s816","s817","s818","s819","s820","s821","s822","s823","s824","s825","shuaishuai"]


for dbname in db_list:

    url_h = url_h1+"{}".format(dbname)
    sel = 'table > tr > td:nth-child(1) > a'
    r = gethtml(url_h)
    s = r.html.find(sel)
    for val in s:
        # print(val.text)
        v = val.text
        m = re.search("_flink$", v)
        if m:
            m = re.search("member_flink$", v)
            if m:  # 过滤member_flink
                pass
            else:
                print(dbname+' '+v)
                f1 = open('日志.txt', 'a', encoding='utf-8')
                f1.write(dbname+' '+v+'\n')
                f1.close()
                sel_n = 'div:nth-child(7)'
                i = 1
                # print(url_h)
                url_flink = url_h1 + '{}&table={}&p={}&charset='.format(dbname,v, i)
                # 获取页数
                r2 = gethtml(url_flink)
                s2 = r2.html.find(sel_n)
                s2 = s2[0].text
                n = re.findall(r'\/\d', s2)[0][1:]  # 取页数
                # print(n)
                n = int(n)
                # 获取数据
                while i <= n:
                    sel = 'table > tr > td:nth-child(4)'
                    # http://www.fjsmled.com/uploads/flink/_btn.php?eanver=mysql_msg&db=a1&table=dede_flink&p=2&charset=
                    url_flink = url_h1 + '{}&table={}&p={}&charset='.format(dbname,v, i)
                    print(url_flink)
                    f2 = open('日志.txt', 'a', encoding='utf-8')
                    f2.write(url_flink+'\n')
                    f2.close()
                    r1 = gethtml(url_flink)
                    s1 = r1.html.find(sel)

                    for val in s1:
                        if (val.text != 'url'):
                            # print(dbname)
                            f = open('网址.txt', 'a', encoding='utf-8')
                            f.write(val.text+'\n')
                            f.close()

                    i = i+1
