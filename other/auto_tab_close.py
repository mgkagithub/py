import pyautogui as pg
from time import sleep 
import sys
import os
pg.FAILSAFE = True
def timers(hours,minutes,seconds):
    print(f"\n\nTimer will close the tab in {(hours*3600)+(minutes*60)+seconds} seconds\n\n")
    print("place your cursor on the window to sync timings")
    sleep(1)
    for i in range(3,0,-1):
        os.system('cls')
        print(f"Timer starts in {i}")
        sleep(1)
    print('Timer started')
    os.system('cls')
    while 1:
        for i in range(60,-1,-1):
            os.system('cls')
            print(f"{hours}:{minutes}:{seconds}")
            sleep(1)
            if i==0:
                minutes-=1
            if minutes==0:
                hours-=1
            if hours==0 and minutes ==0 and seconds==0:
                print("Timer is done")
                pg.keyDown('ctrl')
                pg.press('w')
                pg.keyUp('ctrl')
            return hours , minutes , seconds
def startm():
    pg.leftClick()
hours = int(input("Enter hours: \n"))
minutes = int(input("Enter minutes: \n"))
seconds = int(input("Enter seconds: \n"))
seconds += 1
startm()
timers(hours,minutes,seconds)
print("Music over , closing tab")
print("Tab closed")
