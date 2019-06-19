from requests_html import HTMLSession
import _thread
import time

session = HTMLSession()

url_list=["http://www.atzhuan.com/uploads/160406/web.php?total=10","http://www.guhuituan.com/uploads/170622/web.php?total=10","http://www.5252yue.com/uploads/140607/web.php?total=10","http://qicaipendu.com/uploads/141220/web.php?total=10","http://www.yzxlp.com/uploads/170622/web.php?total=10","http://www.lyrjpx.com/uploads/170622/web.php?total=10","http://xincgy.com/uploads/allimg/130118/web.php?total=10","http://aiche1.com/uploads/140607/web.php?total=10","http://klmlct.com/uploads/allimg/140826/web.php?total=10","http://www.hbcckt.com/uploads/170622/web.php?total=10","http://ywlhjn.com/uploads/flink/web.php?total=10","http://www.dlqinghong.com/uploads/160406/web.php?total=10","http://www.0512mt.com/uploads/160406/web.php?total=10","http://0512mt.com/uploads/media/web.php?total=10","http://pylcmy.com/uploads/121024/web.php?total=10"]

i=15 #循环次数
for j in range(i):
    for url in url_list:
        try:
            print(url)
            session.get(url,timeout=5)
        except:
            pass


#定义线程函数
# def get_url(s_url):
#     print(s_url)
#     session.get(s_url,timeout=5)
    
# try:
#     for url in url_list:        
#         _thread.start_new_thread(get_url,(url,1,))
        
    
# except:
#     print("error")