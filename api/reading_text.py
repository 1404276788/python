#文本文件操作

#url='C:/Users/Administrator/Desktop/web_php.txt'
#url 文本文件路径
def r_text(url):#读取文本文件，数据存放到数组中
    arr=[]
    for line in open(url):
        arr.append(line.strip('\n'))
    return arr

