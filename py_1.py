import api.pachong_article as article


url = 'https://www.cnxiangyan.com/article/15578.html'  # 要爬取的页面

sel_title = 'body > div.main > div > div.pleft > div.m-center-l > h1'  # 文章标题规则
sel_contetn = 'body > div.main > div > div.pleft > div.m-center-l > div.content.con.htmlcontent.arccontent'  # 文章内容规则

r = article.gethtml(url)


title_txt = article.get_article(r, sel_title, False)
print(title_txt)

content_txt = article.getinnerhtml(article.get_article(r, sel_contetn, True))
content_txt = article.html.unescape(content_txt.replace(
    '<i class="arc1"></i> <i class="arc2"></i> <i class="arc3"></i> <i class="arc4"></i>', ''))
# print(content_txt)

# print(title_txt)
