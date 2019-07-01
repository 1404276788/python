#键盘按键监听
import sys, os
from pynput.keyboard import Controller,Key,Listener
import pyautogui as gui
import time

# 监听按压
def on_press(key):
    try: 
        print("正在按压:",format(key.char))

            
    except AttributeError: 
        print("正在按压:",format(key))

# 监听释放  
def on_release(key):     
    print("已经释放:",format(key))     
    if key==Key.f2:  #输入用户名和密码 
        gui.click(x=800, y=406)
        gui.typewrite('admin')
        gui.press("tab")
        gui.typewrite('123456') 
    

    if key==Key.esc:  
        return False 
    


# 开始监听 
def start_listen():
    with Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()


if __name__ == '__main__':     

    # 实例化键盘 
    kb=Controller()

    # 使用键盘输入一个字母
    #kb.press('a')
    #kb.release('a') 

    # 使用键盘输入字符串,注意当前键盘调成英文
    #kb.type("hello world")

    # 使用Key.xxx输入
    kb.press(Key.space)


    # 开始监听,按esc退出监听
    start_listen()
