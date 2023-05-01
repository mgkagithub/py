import os 
import psutil
import subprocess
print(os.getlogin())

def get_battery():
    battery = psutil.sensors_battery()
    if battery:
        return (battery.percent, battery.power_plugged)
    else:
        return None
print(get_battery())

# target_url = "http://192.168.1.15:445/mn/pc/"
# filename = "logs.txt"

# # Define the network drive letter and mount command
# network_drive_letter = "Y:"
# mount_command = f'net use {network_drive_letter} \\\\192.168.1.15\\mn /user:<username> <password>'

# # Mount the network drive if it's not already mounted
# try:
#     if not os.path.exists(network_drive_letter):
#         print(subprocess.check_call(mount_command))
# except subprocess.CalledProcessError as error:
#     print(error)
