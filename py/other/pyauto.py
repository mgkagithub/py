import pyautogui as pg
from time import sleep 
import sys

for i in range(3):
    sleep(1)
    print(i)
    if i == 2:
        print("chants over , tab closed")
        pg.FAILSAFE = True
        pg.keyDown('alt')
        pg.press('F4')
        pg.keyUp('alt')
        sys.exit()