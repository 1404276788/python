import pyautogui as gui
import time
import win32clipboard as wc
import win32api

#获取粘贴板里的内容
def getCopyTxet():
    wc.OpenClipboard()
    copytxet = wc.GetClipboardData()
    wc.CloseClipboard()
    return str(copytxet)

time.sleep(2)
list_arr=['select `value` from a24.dede_sysconfig where varname="cfg_basehost";','select `value` from a25.dede_sysconfig where varname="cfg_basehost";','select `value` from a26.dede_sysconfig where varname="cfg_basehost";','select `value` from a27.dede_sysconfig where varname="cfg_basehost";','select `value` from a28.dede_sysconfig where varname="cfg_basehost";','select `value` from a29.dede_sysconfig where varname="cfg_basehost";','select `value` from a3.dede_sysconfig where varname="cfg_basehost";','select `value` from a30.dede_sysconfig where varname="cfg_basehost";','select `value` from a31.dede_sysconfig where varname="cfg_basehost";','select `value` from a32.dede_sysconfig where varname="cfg_basehost";','select `value` from a33.dede_sysconfig where varname="cfg_basehost";','select `value` from a34.dede_sysconfig where varname="cfg_basehost";','select `value` from a35.dede_sysconfig where varname="cfg_basehost";','select `value` from a36.dede_sysconfig where varname="cfg_basehost";','select `value` from a37.dede_sysconfig where varname="cfg_basehost";','select `value` from a38.dede_sysconfig where varname="cfg_basehost";','select `value` from a39.dede_sysconfig where varname="cfg_basehost";','select `value` from a4.dede_sysconfig where varname="cfg_basehost";','select `value` from a40.dede_sysconfig where varname="cfg_basehost";','select `value` from a41.dede_sysconfig where varname="cfg_basehost";','select `value` from a42.dede_sysconfig where varname="cfg_basehost";','select `value` from a43.dede_sysconfig where varname="cfg_basehost";','select `value` from a44.dede_sysconfig where varname="cfg_basehost";','select `value` from a45.dede_sysconfig where varname="cfg_basehost";','select `value` from a46.dede_sysconfig where varname="cfg_basehost";','select `value` from a47.dede_sysconfig where varname="cfg_basehost";','select `value` from a48.dede_sysconfig where varname="cfg_basehost";','select `value` from a49.dede_sysconfig where varname="cfg_basehost";','select `value` from a5.dede_sysconfig where varname="cfg_basehost";','select `value` from a50.dede_sysconfig where varname="cfg_basehost";','select `value` from a51.dede_sysconfig where varname="cfg_basehost";','select `value` from a52.dede_sysconfig where varname="cfg_basehost";','select `value` from a53.dede_sysconfig where varname="cfg_basehost";','select `value` from a54.dede_sysconfig where varname="cfg_basehost";','select `value` from a55.dede_sysconfig where varname="cfg_basehost";','select `value` from a56.dede_sysconfig where varname="cfg_basehost";','select `value` from a57.dede_sysconfig where varname="cfg_basehost";','select `value` from a58.dede_sysconfig where varname="cfg_basehost";','select `value` from a59.dede_sysconfig where varname="cfg_basehost";','select `value` from a6.dede_sysconfig where varname="cfg_basehost";','select `value` from a60.dede_sysconfig where varname="cfg_basehost";','select `value` from a61.dede_sysconfig where varname="cfg_basehost";','select `value` from a62.dede_sysconfig where varname="cfg_basehost";','select `value` from a63.dede_sysconfig where varname="cfg_basehost";','select `value` from a64.dede_sysconfig where varname="cfg_basehost";','select `value` from a65.dede_sysconfig where varname="cfg_basehost";','select `value` from a66.dede_sysconfig where varname="cfg_basehost";','select `value` from a67.dede_sysconfig where varname="cfg_basehost";','select `value` from a68.dede_sysconfig where varname="cfg_basehost";','select `value` from a69.dede_sysconfig where varname="cfg_basehost";','select `value` from a7.dede_sysconfig where varname="cfg_basehost";','select `value` from a70.dede_sysconfig where varname="cfg_basehost";','select `value` from a71.dede_sysconfig where varname="cfg_basehost";','select `value` from a72.dede_sysconfig where varname="cfg_basehost";','select `value` from a73.dede_sysconfig where varname="cfg_basehost";','select `value` from a74.dede_sysconfig where varname="cfg_basehost";','select `value` from a75.dede_sysconfig where varname="cfg_basehost";','select `value` from a76.dede_sysconfig where varname="cfg_basehost";','select `value` from a77.dede_sysconfig where varname="cfg_basehost";','select `value` from a78.dede_sysconfig where varname="cfg_basehost";','select `value` from a79.dede_sysconfig where varname="cfg_basehost";','select `value` from a8.dede_sysconfig where varname="cfg_basehost";','select `value` from a80.dede_sysconfig where varname="cfg_basehost";','select `value` from a81.dede_sysconfig where varname="cfg_basehost";','select `value` from a82.dede_sysconfig where varname="cfg_basehost";','select `value` from a83.dede_sysconfig where varname="cfg_basehost";','select `value` from a84.dede_sysconfig where varname="cfg_basehost";','select `value` from a85.dede_sysconfig where varname="cfg_basehost";','select `value` from a86.dede_sysconfig where varname="cfg_basehost";','select `value` from a87.dede_sysconfig where varname="cfg_basehost";','select `value` from a88.dede_sysconfig where varname="cfg_basehost";','select `value` from a89.dede_sysconfig where varname="cfg_basehost";','select `value` from a9.dede_sysconfig where varname="cfg_basehost";','select `value` from a90.dede_sysconfig where varname="cfg_basehost";','select `value` from a91.dede_sysconfig where varname="cfg_basehost";','select `value` from a92.dede_sysconfig where varname="cfg_basehost";','select `value` from a93.dede_sysconfig where varname="cfg_basehost";','select `value` from a94.dede_sysconfig where varname="cfg_basehost";','select `value` from a95.dede_sysconfig where varname="cfg_basehost";','select `value` from a96.dede_sysconfig where varname="cfg_basehost";','select `value` from a97.dede_sysconfig where varname="cfg_basehost";','select `value` from a98.dede_sysconfig where varname="cfg_basehost";','select `value` from a99.dede_sysconfig where varname="cfg_basehost";','select `value` from s1122.dede_sysconfig where varname="cfg_basehost";','select `value` from s1123.dede_sysconfig where varname="cfg_basehost";','select `value` from s1124.dede_sysconfig where varname="cfg_basehost";','select `value` from s1125.dede_sysconfig where varname="cfg_basehost";','select `value` from s1126.dede_sysconfig where varname="cfg_basehost";','select `value` from s1127.dede_sysconfig where varname="cfg_basehost";','select `value` from s1128.dede_sysconfig where varname="cfg_basehost";','select `value` from s1129.dede_sysconfig where varname="cfg_basehost";','select `value` from s1130.dede_sysconfig where varname="cfg_basehost";','select `value` from s1131.dede_sysconfig where varname="cfg_basehost";','select `value` from s1132.dede_sysconfig where varname="cfg_basehost";','select `value` from s1133.dede_sysconfig where varname="cfg_basehost";','select `value` from s1134.dede_sysconfig where varname="cfg_basehost";','select `value` from s1135.dede_sysconfig where varname="cfg_basehost";','select `value` from s1136.dede_sysconfig where varname="cfg_basehost";','select `value` from s1137.dede_sysconfig where varname="cfg_basehost";','select `value` from s1138.dede_sysconfig where varname="cfg_basehost";','select `value` from s1139.dede_sysconfig where varname="cfg_basehost";','select `value` from s1140.dede_sysconfig where varname="cfg_basehost";','select `value` from s1141.dede_sysconfig where varname="cfg_basehost";','select `value` from s1142.dede_sysconfig where varname="cfg_basehost";','select `value` from s1143.dede_sysconfig where varname="cfg_basehost";','select `value` from s1144.dede_sysconfig where varname="cfg_basehost";','select `value` from s1145.dede_sysconfig where varname="cfg_basehost";','select `value` from s1146.dede_sysconfig where varname="cfg_basehost";','select `value` from s1147.dede_sysconfig where varname="cfg_basehost";','select `value` from s1148.dede_sysconfig where varname="cfg_basehost";','select `value` from s1149.dede_sysconfig where varname="cfg_basehost";','select `value` from s1150.dede_sysconfig where varname="cfg_basehost";','select `value` from s1151.dede_sysconfig where varname="cfg_basehost";','select `value` from s1152.dede_sysconfig where varname="cfg_basehost";','select `value` from s1153.dede_sysconfig where varname="cfg_basehost";','select `value` from s1154.dede_sysconfig where varname="cfg_basehost";','select `value` from s1155.dede_sysconfig where varname="cfg_basehost";','select `value` from s1156.dede_sysconfig where varname="cfg_basehost";','select `value` from s1157.dede_sysconfig where varname="cfg_basehost";','select `value` from s1158.dede_sysconfig where varname="cfg_basehost";','select `value` from s1159.dede_sysconfig where varname="cfg_basehost";','select `value` from s1160.dede_sysconfig where varname="cfg_basehost";','select `value` from s1161.dede_sysconfig where varname="cfg_basehost";','select `value` from s1162.dede_sysconfig where varname="cfg_basehost";','select `value` from s1163.dede_sysconfig where varname="cfg_basehost";','select `value` from s1164.dede_sysconfig where varname="cfg_basehost";','select `value` from s1165.dede_sysconfig where varname="cfg_basehost";','select `value` from s1166.dede_sysconfig where varname="cfg_basehost";','select `value` from s1167.dede_sysconfig where varname="cfg_basehost";','select `value` from s1168.dede_sysconfig where varname="cfg_basehost";','select `value` from s1169.dede_sysconfig where varname="cfg_basehost";','select `value` from s1170.dede_sysconfig where varname="cfg_basehost";','select `value` from s1171.dede_sysconfig where varname="cfg_basehost";','select `value` from s1172.dede_sysconfig where varname="cfg_basehost";','select `value` from s1173.dede_sysconfig where varname="cfg_basehost";','select `value` from s1174.dede_sysconfig where varname="cfg_basehost";','select `value` from s1175.dede_sysconfig where varname="cfg_basehost";','select `value` from s1176.dede_sysconfig where varname="cfg_basehost";','select `value` from s1177.dede_sysconfig where varname="cfg_basehost";','select `value` from s1178.dede_sysconfig where varname="cfg_basehost";','select `value` from s1179.dede_sysconfig where varname="cfg_basehost";','select `value` from s1180.dede_sysconfig where varname="cfg_basehost";','select `value` from s1181.dede_sysconfig where varname="cfg_basehost";','select `value` from s1182.dede_sysconfig where varname="cfg_basehost";','select `value` from s1183.dede_sysconfig where varname="cfg_basehost";','select `value` from s1184.dede_sysconfig where varname="cfg_basehost";','select `value` from s1185.dede_sysconfig where varname="cfg_basehost";','select `value` from s1186.dede_sysconfig where varname="cfg_basehost";','select `value` from s1187.dede_sysconfig where varname="cfg_basehost";','select `value` from s1188.dede_sysconfig where varname="cfg_basehost";','select `value` from s1189.dede_sysconfig where varname="cfg_basehost";','select `value` from s1190.dede_sysconfig where varname="cfg_basehost";','select `value` from s1191.dede_sysconfig where varname="cfg_basehost";','select `value` from s1192.dede_sysconfig where varname="cfg_basehost";','select `value` from s1193.dede_sysconfig where varname="cfg_basehost";','select `value` from s1194.dede_sysconfig where varname="cfg_basehost";','select `value` from s1195.dede_sysconfig where varname="cfg_basehost";','select `value` from s1196.dede_sysconfig where varname="cfg_basehost";','select `value` from s1197.dede_sysconfig where varname="cfg_basehost";','select `value` from s1198.dede_sysconfig where varname="cfg_basehost";','select `value` from s1199.dede_sysconfig where varname="cfg_basehost";','select `value` from s1200.dede_sysconfig where varname="cfg_basehost";','select `value` from s1201.dede_sysconfig where varname="cfg_basehost";','select `value` from s1202.dede_sysconfig where varname="cfg_basehost";','select `value` from s1203.dede_sysconfig where varname="cfg_basehost";','select `value` from s1204.dede_sysconfig where varname="cfg_basehost";','select `value` from s1205.dede_sysconfig where varname="cfg_basehost";','select `value` from s1206.dede_sysconfig where varname="cfg_basehost";','select `value` from s1207.dede_sysconfig where varname="cfg_basehost";','select `value` from s1208.dede_sysconfig where varname="cfg_basehost";','select `value` from s1209.dede_sysconfig where varname="cfg_basehost";','select `value` from s1210.dede_sysconfig where varname="cfg_basehost";','select `value` from s1211.dede_sysconfig where varname="cfg_basehost";','select `value` from s1212.dede_sysconfig where varname="cfg_basehost";','select `value` from s1213.dede_sysconfig where varname="cfg_basehost";','select `value` from s1214.dede_sysconfig where varname="cfg_basehost";','select `value` from s1215.dede_sysconfig where varname="cfg_basehost";','select `value` from s1216.dede_sysconfig where varname="cfg_basehost";','select `value` from s1217.dede_sysconfig where varname="cfg_basehost";','select `value` from s1218.dede_sysconfig where varname="cfg_basehost";','select `value` from s1219.dede_sysconfig where varname="cfg_basehost";','select `value` from s1220.dede_sysconfig where varname="cfg_basehost";','select `value` from s1221.dede_sysconfig where varname="cfg_basehost";']


for list_arr_s in list_arr:
    # 鼠标点击
    gui.click(x=853, y=310) #坐标处点击
    gui.click(clicks=2) #双击
    # 组合热键
    
    gui.hotkey('ctrl', 'A') #组合热键 按键大小写的区别：大写相当于按住了shift键，小写没有
    time.sleep(1)
    # 按键  
    gui.press("delete") #完成按下和松开的操作

    # 输入操作
    gui.typewrite(list_arr_s)
    time.sleep(0.5)

    gui.click(x=730, y=364)
    time.sleep(1)

    gui.moveTo(630, 450) #鼠标移动绝对位置
    gui.mouseDown() #鼠标按下
    gui.moveRel(320, None, duration=1)
    gui.mouseUp() #鼠标弹起

    time.sleep(0.5)
    gui.hotkey('ctrl','c') #组合热键
    data=getCopyTxet()    
    time.sleep(0.5)
    f=open('1.txt','a',encoding='utf-8')
    f.write(list_arr_s+'|'+data+'\n')
    f.close()


