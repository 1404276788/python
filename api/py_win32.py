# python 获取剪贴板的内容
import win32clipboard as wc
import win32api

# 获取粘贴板里的内容


def getCopyTxet():
    wc.OpenClipboard()
    copytxet = wc.GetClipboardData()
    wc.CloseClipboard()
    return str(copytxet)

# data = getCopyTxet()
# print(data)
