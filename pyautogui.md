### 鼠标操作
```python
# 鼠标点击
gui.click(x=853, y=310) #坐标处点击
gui.click(clicks=2) #双击

#鼠标按下和松开也可以分开处理
pyautogui.mouseDown(x=moveToX, y=moveToY, button='left')
pyautogui.mouseUp(x=moveToX, y=moveToY, button='left')

```
### 键盘操作
```python
import pyautogui

#组合热键
gui.hotkey('ctrl', 'A') #组合热键 按键大小写的区别：大写相当于按住了shift键，小写没有
# 按键 
gui.press("delete") #完成按下和松开的操作
# 输入操作
gui.typewrite('holle')


#返回图片在屏幕上的中心XY轴坐标值
pyautogui.locateCenterOnScreen('pyautogui/looks.png')

```