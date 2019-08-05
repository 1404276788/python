# **python**
	python 学习

## **py_html文件夹** ##
**寄生虫功能文件**
* `dir_url.php`上传到对方服务器，可批量获取html,php文件地址并修改文件
* `main.py`主程序，用于控制`dir_url.php`的功能,比如获取当前目录及以下的所有文件路径，批量修改指定文件类型的文件内容


**依赖文件：**
* `py_get_db.py`请求数据库数据，用于控制php文件的写入内容
* `py_get_http.py`文件是`post`请求功能与`get`请求功能

**文件说明**
* `py_win32.py`获取剪贴板内容.
* `wenjianduibi.py`文件对比，目标文件与源文件对比，如果源文件中有，则跳过，如果没有，则把没有的那行数据单独存放到文件中记录.
* `pyzhi_img.py`网页图片爬取，并保存到当前程序的img文件夹中，img文件夹需要自己创建.
* `py_plth.py`,`body_update.py`dedecms数据库文章内容批量替换.
* `py_input.py`键盘监听并执行对应的操作
