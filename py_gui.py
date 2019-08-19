import pyautogui as gui
import time
import win32clipboard as wc
import win32api

# 获取粘贴板里的内容


def getCopyTxet():
    wc.OpenClipboard()
    copytxet = wc.GetClipboardData()
    wc.CloseClipboard()
    return str(copytxet)


time.sleep(2)
list_arr = [
    'select `value` from a24.dede_sysconfig where varname="cfg_basehost";']


for list_arr_s in list_arr:
    # 鼠标点击
    gui.click(x=853, y=310)  # 坐标处点击
    gui.click(clicks=2)  # 双击
    # 组合热键

    gui.hotkey('ctrl', 'A')  # 组合热键 按键大小写的区别：大写相当于按住了shift键，小写没有
    time.sleep(1)
    # 按键
    gui.press("delete")  # 完成按下和松开的操作

    # 输入操作
    gui.typewrite(list_arr_s)
    time.sleep(0.5)

    gui.click(x=730, y=364)
    time.sleep(1)

    gui.moveTo(630, 450)  # 鼠标移动绝对位置
    gui.mouseDown()  # 鼠标按下
    gui.moveRel(320, None, duration=1)
    gui.mouseUp()  # 鼠标弹起

    time.sleep(0.5)
    gui.hotkey('ctrl', 'c')  # 组合热键
    data = getCopyTxet()
    time.sleep(0.5)
    f = open('1.txt', 'a', encoding='utf-8')
    f.write(list_arr_s+'|'+data+'\n')
    f.close()
