from requests_html import HTMLSession
import _thread
import time
import re

session = HTMLSession()

url_list=["http://www.qdtoefl.com/a/shuaji/web.php?total=20","http://sydctj.com/tuiguang/201303/web.php?total=20","http://qw3921.com/chanpin/web.php?total=20","http://www.spcysh.com/a/lianxiwomen/web.php?total=20","http://bggdpj.com/a/toutiao/web.php?total=20","http://www.csmmsj.com/a/guzhang/web.php?total=20","http://www.57digo.com/a/shezhi/web.php?total=20","http://sywykzs.com/a/ruiguandian/web.php?total=20","http://5199ys.com/mote/web.php?total=20","http://qdysh.com/a/zhongyijibing/web.php?total=20","http://yukare.com/gongsi/web.php?total=20","http://www.necsell.com/a/banquanshenming/web.php?total=20","http://zhhtzz.com/jiancha/zam/web.php?total=20","http://youhuamall.com/html/gonggao/web.php?total=20","http://sjzyksm.com/a/qita/web.php?total=20","http://mtxjz.com/aiqingsanwen/web.php?total=20","http://359tao.com/a/guanyuwomen/web.php?total=20","http://www.tianshuiot.com/a/meinv/web.php?total=20","http://www.sm887.com/a/mingrenmingyan/web.php?total=20","http://www.sm387.com/a/jiaocheng/fuwuqi/web.php?total=20","http://www.723123hd.com/a/nvxing/web.php?total=20","http://www.hh-sh.net/front/web.php?total=20","http://www.guxinyuan.net/a/qiwen/web.php?total=20","http://www.zxingroup.com/a/qiwen/web.php?total=20","http://www.gzcx8013.com/a/meinv/web.php?total=20","http://www.syssxg.com/a/msh/web.php?total=20","http://www.1y365.net/a/qiwen/web.php?total=20"]


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