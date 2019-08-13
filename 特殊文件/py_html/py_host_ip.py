# 批量查询域名ip
from socket import gethostbyname
import reading_text as reading  # 读取文件内容转为数组

# url='C:/Users/Administrator/Desktop/web_php.txt'
# url 文本文件路径


# def r_text(url):  # 读取文本文件，数据存放到数组中
#     arr = []
#     for line in open(url):
#         arr.append(line.strip('\n'))
#     return arr

txturl = 'urllist.txt'
arr = reading.r_text(txturl)
# print(arr)

for url in arr:
    print(url)
    try:
        host = gethostbyname(url)
        if host:
            f1 = open('url_ip.txt', 'a', encoding='utf-8')
            f1.write(url+' '+host+'\n')
            f1.close()
    except Exception as e:
        pass
