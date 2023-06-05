import time
import datetime
import psutil
import win32com.client
import requests
import wmi
import json
import subprocess
import pygetwindow as gw
import pyperclip
import shutil

# Function to get the logged-in user name
def get_logged_in_user_name():
    shell = win32com.client.Dispatch("WScript.Shell")
    username = shell.ExpandEnvironmentStrings("%USERNAME%")
    return username

# Function to get the battery status
def get_battery():
    battery = psutil.sensors_battery()
    percent = battery.percent
    power_plugged = battery.power_plugged
    if power_plugged:
        status = "Charging"
    else:
        status = "Not Charging"
    return percent, status

# Function to get the connected WiFi name
def get_wifi_name():
    wmi_obj = wmi.WMI()
    wifi_networks = wmi_obj.Win32_NetworkAdapter(NetConnectionID="Wi-Fi")
    # wifi_name = wifi_networks[0].NetConnectionID
    wifi_name = 'smng'
    return wifi_name

# Function to get the connected Bluetooth devices
def get_bluetooth_name():
    wmi_obj = wmi.WMI()
    bluetooth_devices = wmi_obj.Win32_PnPEntity(Name__contains="Bluetooth")
    bluetooth_names = [device.Name for device in bluetooth_devices]
    return bluetooth_names

# Function to get the current date and time
def get_date_time():
    now = datetime.datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return date_time

# Function to get a list of currently running processes
def get_process_list():
    processes = []
    for proc in psutil.process_iter(['name']):
        processes.append(proc.info['name'])
    return processes

# Function to get the IP location using ip-api.com
def get_ip_location():
    response = requests.get('http://ip-api.com/json/')
    location_data = json.loads(response.text)
    ip_location = location_data['city']
    return ip_location

# Function to get the list of installed programs
def get_installed_programs():
    programs = subprocess.check_output(['wmic', 'product', 'get', 'name']).decode('utf-8').split('\n')
    programs = [program.strip() for program in programs if program.strip()]
    return programs

# Function to get the list of recent files accessed
def get_recent_files():
    shell = win32com.client.Dispatch("WScript.Shell")
    recent_files = shell.SpecialFolders("Recent")
    files = os.listdir(recent_files)
    return files

# Function to get the system resources usage
def get_system_resources():
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    return cpu_usage, memory_usage, disk_usage

# Function to get the list of connected USB devices
def get_usb_devices():
    usb_devices = wmi.WMI().Win32_USBControllerDevice()
    devices = [device.Dependent.Caption for device in usb_devices]
    return devices

# Function to get the current weather
def get_weather():
    response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=city_name&appid=your_api_key')
    weather_data = json.loads(response.text)
    weather = weather_data['weather'][0]['description']
    return weather

# Function to get the title of the active window
def get_active_window_title():
    active_window = gw.getActiveWindow()
    title = active_window.title
    return title

# Function to get the contents of the clipboard
def get_clipboard_contents():
    clipboard_contents = pyperclip.paste()
    return clipboard_contents

# Function to get disk space information
def get_disk_space():
    total, used, free = shutil.disk_usage("/")
    return total, used, free

# Function to get network activity
def get_network_activity():
    network_activity = psutil.net_io_counters()
    sent = network_activity.bytes_sent
    received = network_activity.bytes_recv
    return sent, received

# Function to get the list of connected devices
def get_connected_devices():
    wmi_obj = wmi.WMI()
    devices = wmi_obj.Win32_PnPEntity()
    connected_devices = [device.Description for device in devices]
    return connected_devices

# Function to get system logs
def get_system_logs():
    logs = subprocess.check_output(['wevtutil', 'qe', 'System', '/q:*[System[Level=2]]']).decode('utf-8')
    return logs

# Function to get startup programs
def get_startup_programs():
    startup_folder = shell.SpecialFolders("Startup")
    programs = os.listdir(startup_folder)
    return programs

# Function to pause the program
def pause_program():
    while True:
        time.sleep(3600)

# Function to resume the program
def resume_program():
    main()

# Function to shut down the laptop
def shutdown_laptop():
    subprocess.call(["shutdown", "/s"])

# Function to restart the laptop
def restart_laptop():
    subprocess.call(["shutdown", "/r"])

# Function to log the gathered information to a file
def log_to_file(log_file, data):
    with open(log_file, 'a') as file:
        file.write(data + '\n')

# Main program
def main():
    log_file = "logs.txt"

    # Check if connected to the internet
    try:
        requests.get('https://www.google.com', timeout=5)
        connected_to_internet = True
    except requests.ConnectionError:
        connected_to_internet = False

    if not connected_to_internet:
        print("Not connected to the internet. Exiting...")
        return

    while True:
        logged_in_user = get_logged_in_user_name()
        percent, status = get_battery()
        wifi_name = get_wifi_name()
        bluetooth_names = get_bluetooth_name()
        date_time = get_date_time()
        processes = get_process_list()
        ip_location = get_ip_location()
        installed_programs = get_installed_programs()
        recent_files = get_recent_files()
        cpu_usage, memory_usage, disk_usage = get_system_resources()
        usb_devices = get_usb_devices()
        weather = get_weather()
        active_window_title = get_active_window_title()
        clipboard_contents = get_clipboard_contents()
        total, used, free = get_disk_space()
        sent, received = get_network_activity()
        connected_devices = get_connected_devices()
        system_logs = get_system_logs()
        startup_programs = get_startup_programs()

        # Prepare the log entry
        log_entry = f"Logged-in User: {logged_in_user}\n"
        log_entry += f"Battery: {percent}% ({status})\n"
        log_entry += f"WiFi: {wifi_name}\n"
        log_entry += f"Bluetooth: {', '.join(bluetooth_names)}\n"
        log_entry += f"Date/Time: {date_time}\n"
        log_entry += f"Processes: {', '.join(processes)}\n"
        log_entry += f"IP Location: {ip_location}\n"
        log_entry += f"Installed Programs: {', '.join(installed_programs)}\n"
        log_entry += f"Recent Files: {', '.join(recent_files)}\n"
        log_entry += f"CPU Usage: {cpu_usage}%\n"
        log_entry += f"Memory Usage: {memory_usage}%\n"
        log_entry += f"Disk Usage: {disk_usage}%\n"
        log_entry += f"USB Devices: {', '.join(usb_devices)}\n"
        log_entry += f"Weather: {weather}\n"
        log_entry += f"Active Window Title: {active_window_title}\n"
        log_entry += f"Clipboard Contents: {clipboard_contents}\n"
        log_entry += f"Disk Space: Total={total}, Used={used}, Free={free}\n"
        log_entry += f"Network Activity: Sent={sent}, Received={received}\n"
        log_entry += f"Connected Devices: {', '.join(connected_devices)}\n"
        log_entry += f"System Logs: {system_logs}\n"
        log_entry += f"Startup Programs: {', '.join(startup_programs)}\n"

        # Log the entry
        log_to_file(log_file, log_entry)

        # Wait for 1 hour
        time.sleep(3600)

if __name__ == "__main__":
    main()
