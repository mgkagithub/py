import datetime
import time
from time import sleep
import pyautogui as pg 
import webbrowser
current_time = datetime.datetime.now()
formatted_time = current_time.strftime('%H:%M:%S')
print(formatted_time)
if formatted_time[0:2] == '08':
    webbrowser.open_new_tab("https://fountane.keka.com/#/me/attendance/logs")

