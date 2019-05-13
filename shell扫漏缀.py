# 获取页面状态码
import requests

louzhui='C:/Users/Administrator/Desktop/louzhui.txt'  #漏缀文件名
url_txt='C:/Users/Administrator/Desktop/1.txt'  #网址文件

#超时重试  3次
def getcode(url):
    i=0
    while i<3:
        try:
            r=requests.get(url,timeout=3).status_code  #请求时间5s
            return r
        except:            
            i+=1
            print('重新连接'+str(i))      # i 是数字，不能与字符串进行运算，需要使用str()转换成字符串 


louzhui_arr=[]
for line_f in open(louzhui):
    line_f_arr=line_f.split('|')
    # print(line_f_arr[1])
    # line_f_arr[1]=line_f_arr[1].replace('/n','')
    louzhui_arr.append(line_f_arr)

# print(louzhui_arr)
for line_html in open(url_txt):
    # print(line_html,end='')
    a='http'
    res=a in line_html
    if res:
        for lz in louzhui_arr:            
            r=getcode(line_html+lz[0])
            if r==200:
                print(line_html+lz[0]+'|'+lz[1])


        
# r=requests.get(url='http://www.zykj999.com/languages/zh_cn/convert/shopex49.php').status_code
# print(r)