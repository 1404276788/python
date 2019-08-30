import api.pachong_article as article


url = 'http://szkb.gansudaily.com.cn/system/2018/10/23/017069523.shtml'  # 要爬取的页面

sel_title = '#container > h1'  # 文章标题规则
sel_contetn = '#conter2018'  # 文章内容规则

r = article.gethtml(url)


title_txt = article.get_article(r, sel_title, False)
# print(title_txt)

content_txt = article.getinnerhtml(article.get_article(r, sel_contetn, True))
# content_txt = article.html.unescape(content_txt.replace(
#     '<i class="arc1"></i> <i class="arc2"></i> <i class="arc3"></i> <i class="arc4"></i>', ''))
f = open('C:/Users/Administrator/Desktop/文章/' +
         title_txt+'.txt', 'a', encoding='utf-8')
f.write(content_txt)
f.close()
# print(content_txt)

# print(title_txt)
