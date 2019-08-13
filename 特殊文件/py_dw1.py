# 爬取大马页面中的所有数据库中友链
# coding:utf-8
from requests_html import HTMLSession
import requests
import urllib
import os
import re


session = HTMLSession()
url_h1 = 'http://www.jotonsoft.com/plus/Teams.php?eanver=mysql_msg&db='

headers = {
    "cookie": "envlpass=aafe421b8ad20fe391be17a529c844c2; serveru=www.jotonsoft.com%2Fplus%2FTeams.php; serverp=cc11; m_eanverhost=localhost; m_eanverport=3306; m_eanveruser=shuaishuai; m_eanverpass=123456; PHPSESSID=d5t5m5c8jmj5l02g0su5fkmhn0; _csrf_name_29ac59d6=2c10c320074989ea39d98e909bf4e54d; _csrf_name_29ac59d6__ckMd5=42b2972e0012c94b; DedeUserID=1; DedeUserID__ckMd5=58eeade475922d2c; DedeLoginTime=1565658137; DedeLoginTime__ckMd5=f17579dad2241a6d; ENV_GOBACK_URL=%2Fadmindede%2Fmedia_main.php%3Fdopost%3Dfilemanager"
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


db_list = ["a00102","a00138","a00166","a00167","a00168","a0070","a0101","a0103","a0104","a0106","a0109","a0110","a0111","a0112","a0114","a0117","a0118","a0119","a0121","a0123","a0124","a0125","a0126","a0129","a0130","a0131","a0133","a0135","a0136","a0137","a0138","a0140","a0141","a0142","a0143","a0144","a0148","a0149","a0150","a0153","a0154","a0157","a0159","a0160","a0161","a0165","a0166","a0167","a0168","a0169","a0170","a0171","a0172","a041","a042","a044","a045","a047","a048","a049","a0490","a050","a0500","a051","a052","a053","a054","a055","a056","a058","a059","a060","a062","a064","a065","a066","a067","a069","a070","a072","a074","a075","a076","a077","a078","a079","a080","a081","a082","a084","a085","a087","a088","a089","a090","a091","a092","a093","a094","a095","a100","a102","a105","a107","a108","a113","a115","a116","a120","a122","a127","a128","a132","a134","a139","a145","a146","a147","a151","a152","a155","a156","a158","a162","a163","a164","a172","a39","a40","a41","a42","a44","a45","a46","a47","a48","a57","a61","a63","a68","a71","a73","a83","a86","a96","a97","a98","a99","blogs","k00158","k0042","k0045","k0046","k0047","k0048","k0102","k0158","k0163","k0164","k0165","k0166","k0167","k039","k040","k041","k044","k049","k086","k100","k101","k103","k104","k105","k106","k107","k108","k109","k110","k111","k112","k113","k114","k115","k116","k117","k118","k119","k120","k121","k122","k123","k124","k125","k126","k127","k128","k129","k130","k131","k132","k133","k134","k135","k136","k137","k138","k139","k140","k141","k142","k143","k144","k145","k146","k147","k148","k149","k150","k151","k152","k153","k154","k155","k156","k157","k159","k35","k36","k37","k38","k43","k50","k51","k52","k53","k54","k55","k56","k57","k58","k59","k60","k61","k62","k63","k64","k65","k66","k67","k68","k69","k70","k71","k72","k73","k74","k75","k76","k77","k78","k79","k80","k81","k82","k83","k84","k85","k86","k87","k88","k89","k90","k91","k92","k93","k94","k95","k96","k97","k98","k99","money","mysql","performance_schema","s45","shuaishuai","travel","travelgame"]


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
