
# PyAutoGUI is essentially a Python package that works across Windows, MacOS X and Linux which 
# provides the ability to simulate mouse cursor moves and clicks as well as keyboard button presses.

import pyautogui
import time
time.sleep(4)
count=0
while count<=5:
    pyautogui.typewrite(" HELLO "+str(count))
    pyautogui.press("enter")
    count=count
    
                   