#url请求功能
from requests_html import HTMLSession
import xlwt
import re
import time
import ssl

ssl._create_default_https_context=ssl._create_unverified_context

session=HTMLSession()   #建立会话


  


def gethtml_30(url,headers):
    i=0
    while i<3:
        try:
            r=session.get(url,headers=headers,timeout=30)  #请求时间
            return r
        except:            
            i+=1
            print('重新连接'+str(i))      # i 是数字，不能与字符串进行运算，需要使用str()转换成字符串 

nump=18
while nump<44:
    new_workbook=xlwt.Workbook() #新建工作簿
    worksheet=new_workbook.add_sheet('news_test') #新建工作表
    worksheet.write(0,0,'域名')     #（0，0）的位置写入数据 '域名'
    worksheet.write(0,1,'pc')    
    worksheet.write(0,2,'m')  
    url = 'http://apiv2.shawdo.com:8080/v2admin/website/website/?p={}&q='.format(nump)
    headers = {
        "Cookie": "csrftoken=tr5s4odSD4iqyUnsmSWtlEkMD3wdzrM7eQ9NmKC82brMEYRCwoRr65u1Pbgg3c0d; sessionid=vmh8eu3wu0cy5ho9i6jphv2vujbhgunf"
    }
    r= gethtml_30(url,headers)
    admin='#result_list > tbody > tr > td.field-pc_admin_a'
    pc='#result_list > tbody > tr > td.field-web_template.nowrap'
    m='#result_list > tbody > tr > td.field-m_template.nowrap'
    page='#changelist-form > p > a.end'
    # num= gethtml_30(url,headers)
    # resnum=num.html.find(page).text

    index=0
    admin_list=r.html.find(admin)
    for admintext in admin_list:
        s=admintext.text
        worksheet.write(index+1,0,s)
        index=index+1

    index=0
    pc_list=r.html.find(pc)
    for pctext in pc_list:    
        s=pctext.text
        worksheet.write(index+1,1,s)
        index=index+1

    index=0
    m_list=r.html.find(m)
    for mtext in m_list:    
        s=mtext.text    
        worksheet.write(index+1,2,s)
        index=index+1


    new_workbook.save('{}.xls'.format(nump+1)) #保存位置
    nump += 1;