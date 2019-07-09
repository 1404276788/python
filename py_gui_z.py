import pyautogui as gui
import time

# gui.mouseDown(140,275,button='left') #按下左键

# gui.moveRel(200,None,duration=0.5)

# gui.moveRel(None,200,duration=0.5)

# gui.moveRel(-200,None,duration=0.5)

# gui.moveRel(None,-200,duration=0.5)

# gui.moveRel(200,200,duration=0.5)

# gui.mouseUp(None,None,button='left')

# gui.dragRel(None,100,button='left')

# gui.dragRel(100,None,button='left')

# gui.dragRel(None,-100,button='left')

# gui.dragRel(-100,None,button='left')


gui.mouseDown(36,220,button='left') #按下左键

i=1
while i<=5:
    gui.dragRel(100,None,button='left')
    gui.dragRel(None,100,button='left')
    i=i+1

i=1
while i<=5:
    gui.dragRel(100,None,button='left')
    gui.dragRel(None,-100,button='left')
    i=i+1

gui.dragRel(100,None,button='left')
gui.dragTo(36,220,button='left')