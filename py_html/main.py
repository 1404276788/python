import py_get_http as myget #引入文件
import py_get_db as mydb

url='http://www.chen02.com/dir_url.php'
r=myget.posthtml_30(url,{'m':1}) 

s=r.html.text
s_list=s.split('\n')

print('修改中...')
f=open('1.txt','a',encoding='utf-8')
for val in s_list:
    htmls=mydb.db_htmls() #取数据
    r1=myget.posthtml_5(url,{'file':val,'htmls':htmls})
    s1=r1.text
    result='修改完成' in s1
    if result:
        f.write(s1+'\n')

f.close()
print('修改完成')

