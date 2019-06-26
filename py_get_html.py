# 页面循环请求
from requests_html import HTMLSession
import _thread
import time
import re

session = HTMLSession()

url_list=["http://www.detectsoft.com/a/meinv/web.php?total=20","http://www.zhuanhi.com/a/qiwen/web.php?total=20","http://www.yima178.com/a/toutiao/web.php?total=20","http://www.cungulaila.com/jieshao/web.php?total=20","http://www.jyad88.com/a/qiwen/web.php?total=20","http://www.1tgou.com/a/toutiao/web.php?total=20","http://www.dhssjx.com/article/zonghe/web.php?total=20","http://www.suckj.com/a/qiwen/web.php?total=20","http://www.yg39.net/yinhang/web.php?total=20","http://www.yskaowo.com/gongzuodongtai/web.php?total=20","http://www.tl6800.com/a/fazhishenghuo/web.php?total=20","http://www.yinkuchina.com/a/weinongfuwu/zaishengziyuan/web.php?total=20","http://www.ryzg168.com/a/tashan/web.php?total=20","http://www.jpcjujia.com/a/qiwen/web.php?total=20","http://www.qztwsz.com/about/ad/web.php?total=20","http://www.lbczg.com/a/xinqingshuoshuo/web.php?total=20","http://www.qianweicl.com/a/toutiao/web.php?total=20","http://www.lv008.net/yingwenyulu/web.php?total=20","http://www.xacsgd.com/gongsi/web.php?total=20","http://www.gzn10.com/a/xinqingshuoshuo/web.php?total=20","http://www.112623.com/a/shenghuo/web.php?total=20","http://www.112621.com/data/mail/web.php?total=20","http://www.lshxdc.com/a/meinv/20170622/web.php?total=20","http://www.binyichou.com/a/meinv/web.php?total=20","http://www.rexuetuan.com/a/qiwen/web.php?total=20"]


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


i=20 #循环次数
get_url_html(i)
dw()