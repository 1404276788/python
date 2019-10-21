# 文件对比，目标文件与源文件对比，如果源文件中有，则记录，如果没有，跳过
import re

# 源文件
txt = "C:\\Users\\admin\\Desktop\\snsnb_err.txt"
# 目标文件
txt1 = "snsnb\\portal_article_title.txt"
# 存放地址
txt_jg = '对比结果.txt'

f = open(txt, 'r', encoding='utf-8')  # 读取文本文件中的内容
s = f.read()  # 内容赋值给变量


for line in open(txt1):
    # print(line,end='')
    r_txt = line.strip('\n')
    result = r_txt in s  # 判断指定的字符串是否在文本中，返回布尔值
    # print(result)
    if result == False:  # 目标文件中的内容不存在源文件中，存放
        f = open(txt_jg, 'a', encoding='utf-8')
        f.write(line)
        f.close()
