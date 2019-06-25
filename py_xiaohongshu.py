#测试爬取小红书数据
from requests_html import HTMLSession,HTML

import urllib.request

session = HTMLSession()
url="https://www.xiaohongshu.com/fe_api/burdock/v1/search/note?keyword=代孕&page_size=20"
# url='https://www.xiaohongshu.com/search_result/%E4%BB%A3%E5%AD%95'
headers={
    "cookie":"xhsTrackerId=8447ca41-4dc5-4d4d-cd3c-787ee5dfc163; Hm_lvt_9df7d19786b04345ae62033bd17f6278=1560234436,1560235362,1560235896,1560236101; Hm_lvt_d0ae755ac51e3c5ff9b1596b0c09c826=1560235362,1560235896,1560236101; Hm_lpvt_d0ae755ac51e3c5ff9b1596b0c09c826=1560236101; extra_exp_ids=; xhs_spses.5dde=*; Hm_lpvt_9df7d19786b04345ae62033bd17f6278=1560308154; xhs_spid.5dde=3890b6a0d8fe39b0.1560234436.2.1560308157.1560236105.1b726a3e-8be7-4ebf-b0a6-2d828b1101dd",
    "x-sign":"X78bc4e8c6106155783b5e50efac581dd"
}
#r = session.get(url=url,headers=headers)
#r.encoding="utf-8"
#print(r.html.html)

r = session.get(url=url,headers=headers)
print(r.headers)

# file=urllib.request.urlopen(url)
# print(val)


