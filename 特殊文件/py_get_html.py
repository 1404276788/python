# 页面循环请求
from requests_html import HTMLSession
import _thread
import time
import re

session = HTMLSession()

url_list=["http://www.cgjy01.com/chuangyishalong/web.php?total=20","http://www.chung01.com/a/shangye/20190425/web.php?total=20","http://www.bjtsdjz.com/bizhi/aiawuw/web.php?total=20","http://www.dzhqspc.com/qiwenqushi/web.php?total=20","http://www.beioejia.com/a/shangye/web.php?total=20","http://www.jojupu.com/guojiaxinwen/20190725/web.php?total=20","http://www.hbbidding.net/a/android/web.php?total=20","http://www.ksyushuo.com/a/hot/web.php?total=20","http://www.china-ret.net/a/guandian/web.php?total=20","http://www.xian400.net/shehuijujiao/web.php?total=20","http://www.laide66.com/about/yl/web.php?total=20","http://www.yajin01.com/a/guandian/web.php?total=20","http://www.yajin88.com/a/muying/web.php?total=20","http://www.popomi.net/chuangyishalong/web.php?total=20","http://www.qdzcfjwz.com/dapeishuo/web.php?total=20","http://www.soupaish.com/a/zhinen/web.php?total=20","http://www.techemc.com/365tiyuwangtou/web.php?total=20","http://www.tjtcxyhg.com/lxwm/web.php?total=20","http://www.ht-fluid.com/bizhi/web.php?total=20","http://www.bjjyhengye.com/jiaoyizhinan/web.php?total=20","http://www.haockjfw.com/bxww/web.php?total=20","http://www.guarts.com/a/shangye/web.php?total=20","http://www.4000432055.com/about/web.php?total=20","http://www.tiantianxo.com/renwu/web.php?total=20","http://www.hengfengzl.com/about/html/web.php?total=20","http://www.jyxtfz.com/meizi/web.php?total=20","http://www.klyigu.com/about/notice/web.php?total=20","http://www.xnymypd.com/a/wlyx/web.php?total=20","http://www.qdanpay.com/html/Agedcare/web.php?total=20","http://www.gljszl.com/a/zixun/web.php?total=20"]


dirname='C:/Users/Administrator/Desktop/s' #文件夹路径

def gethtml(url):
    i=0
    while i<3:
        try:
            r=session.get(url,timeout=5)  #请求时间5s
            return r
        except:            
            i+=1
            print('重新连接'+str(i))      # i 是数字，不能与字符串进行运算，需要使用str()转换成字符串 
    #最终请求失败返回并记录
    f=open(dirname+'/'+'err.txt','a',encoding='utf-8') #请求最后失败放入到err.txt文件中
    f.write(url+'\n')
    f.close()

#正则 zstr:正则 s:替换成什么内容  stxt：需要替换的内容
def zz(zstr,s,stxt):
    strinfo=re.compile(zstr) #正则匹配最后一个斜杠后的内容
    url_q=strinfo.sub(s,stxt)
    return url_q

# 请求路径去生成寄生虫文件

def get_url_html(i):
    for j in range(i):
        for url in url_list:
            try:
                print(url)
                session.get(url,timeout=5)
            except:
                pass
#--------------------------------------------------
#生成完毕后，判断生成数量是否达到目标，如果没有达到，再次生成，如果达到，下载到本地
#--------------------------------------------------
def dw():
    url_q=zz('[^/]+(?!.*/)','',url_list[0])+'/text.txt' ##正则匹配最后一个斜杠后的内容
    r=gethtml(url_q)
    # print(r.html.text)
    s=r.html.text
    list_url_q=s.split(' ')
    print(len(list_url_q))
    l_len=len(list_url_q)  #生成的个数

    #如果生成的文件大于1000，就下载下来
    if l_len>1000:
        for url_1 in url_list:
            url_1=zz('[^/]+(?!.*/)','',url_1)+'/text.txt'
            res=gethtml(url_1) #获取内容
            text=zz('[\s]','\n',res.html.text) #获取的内容按行存储
            f=open(dirname+'/'+str(float(time.time())*1000)+'.txt','w',encoding='utf-8') #请求最后失败放入到err.txt文件中
            f.write(text+'\n')
            f.close()
        
    else:
        get_url_html(1)
        dw()

i=10 #循环次数
get_url_html(i)
dw()