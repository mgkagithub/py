import pyautogui as pg
from time import sleep 
import sys
import os 
hours = int(input("Enter hours: \n"))
hours = hours*3600
minutes = int(input("Enter minutes: \n"))
minutes = minutes*60
seconds = int(input("Enter seconds: \n"))
total_seconds = hours + minutes + seconds
print(f"\n\nTimer will close the tab in {total_seconds} seconds\n\n")
sleep(1)
for i in range(3,0,-1):
    os.system('cls')
    print(f"Timer starts in {i}")
    sleep(1)
print('Timer started')
os.system('cls')
for i in range(1,total_seconds):
    print(i)
    sleep(1)
    os.system('cls')
    if i == total_seconds-1:
        print("Music over , closing tab")
        pg.FAILSAFE = True
        pg.keyDown('ctrl')
        pg.press('w')
        pg.keyUp('ctrl')
        print("Tab closed")
        sys.exit()