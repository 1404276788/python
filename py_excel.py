# 键盘按键监听
# import api.py_win32 as pycopy  # 获取剪贴板内容 getCopyTxet()
import api.reading_text as readtxt  # 获取文件中的内容转为数组 r_text()
import sys
import os
from pynput.keyboard import Controller, Key, Listener
import pyautogui as gui
import time
import pyperclip

# 监听按压

keys = readtxt.r_text('C:/Users/Administrator/Desktop/已完成.txt')

f9zt = 1


def on_press(key):
    try:
        # if key == key.esc or key == key.f9:
        print("正在按压:", format(key.char))

    except AttributeError:
        # if key == key.esc or key == key.f9:
        print("正在按压:", format(key))

# 监听释放


def on_release(key):
    # if key == key.esc or key == key.f9:
    print("已经释放:", format(key))
    if key == Key.f9:  # 输入用户名和密码
        global f9zt
        global keys
        # f10 h l h t
        if f9zt == 1:

            for i, v in enumerate(keys):
                if i < 160:
                    pass

                if i >= 200 and i < 220:
                    time.sleep(1)
                    gui.press("f10")
                    time.sleep(1)
                    gui.press("h")
                    time.sleep(1)
                    gui.press("l")
                    time.sleep(1)
                    gui.press("h")
                    time.sleep(1)
                    gui.press("t")
                    time.sleep(4.5)
                    gui.press("delete")
                    pyperclip.copy(v)
                    # pyperclip.paste()
                    # gui.typewrite(v)
                    gui.hotkey('ctrl', 'v')
                    gui.press("enter")
                    f = open('chuli.txt', 'a', encoding='utf-8')
                    print(v)
                    f.write(v+'\n')
                    f.close()
                    time.sleep(3)

                if i >= 220:
                    break

    if key == Key.esc:
        return False


# 开始监听
def start_listen():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == '__main__':

    # 实例化键盘
    kb = Controller()

    # 使用键盘输入一个字母
    # kb.press('a')
    # kb.release('a')

    # 使用键盘输入字符串,注意当前键盘调成英文
    #kb.type("hello world")

    # 使用Key.xxx输入
    kb.press(Key.space)

    # 开始监听,按esc退出监听
    start_listen()
