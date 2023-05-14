import pyautogui as pg
from time import sleep 
import sys

for i in range(16200):
    sleep(1)
    print(i)
    if i == 16199:
        print("music over , tab closed")
        pg.FAILSAFE = True
        pg.keyDown('alt')
        pg.press('F4')
        pg.keyUp('alt')
        sys.exit()