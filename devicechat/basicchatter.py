import os
import requests
import pyperclip
import base64
import re
import json
import time 
# Replace '192.168.1.15' with the public IP address or domain name of your Raspberry Pi (Nakama)
NAKAMA_IP = '192.168.1.23'
# Replace 5001 with the chosen port number for your Flask server
NAKAMA_PORT = 5001

def classify_clipboard_content(clipboard_content):
    # Check for URLs
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    if url_pattern.match(clipboard_content):
        return 'url'
    
    # Check for JSON data
    try:
        json.loads(clipboard_content)
        return 'json'
    except json.JSONDecodeError:
        pass

    # Check for numbers
    if clipboard_content.replace('.', '').isdigit():
        return 'number'

    # Check for alphanumeric data
    if clipboard_content.isalnum():
        return 'alphanumeric'

    # Default to plain text if no specific type is detected
    return 'text'

def send_message(message, message_type):
    if message_type == 'image':
        with open(message, 'rb') as file:
            binary_data = file.read()
            base64_data = base64.b64encode(binary_data).decode('utf-8')
            data = {'message': base64_data, 'type': 'file', 'file_name': message}
    else:
        data = {'message': message, 'type': message_type}

    url = f'http://{NAKAMA_IP}:{NAKAMA_PORT}/send_message'
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print('synced')
    else:
        print('Failed to send message.')


def send_file(file_path):
    with open(file_path, 'rb') as file:
        binary_data = file.read()
        base64_data = base64.b64encode(binary_data).decode('utf-8')
        url = f'http://{NAKAMA_IP}:{NAKAMA_PORT}/send_message'
        data = {'message': base64_data, 'type': 'file', 'file_name': file_path}
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print('File sent successfully.')
        else:
            print('Failed to send file.')

def get_messages():
    url = f'http://{NAKAMA_IP}:{NAKAMA_PORT}/get_messages'
    response = requests.get(url)
    if response.status_code == 200:
        messages = response.json()
        print('Received messages:')
        for message in messages:
            if message.get('type') == 'file':
                file_data = base64.b64decode(message['message'])
                file_name = message['file_name']
                with open(file_name, 'wb') as file:
                    file.write(file_data)
                print(f'Received file: {file_name}')
            else:
                print(message['message'])
    else:
        print('Failed to get messages.')

def get_clipboard_content():
    clipboard_content = pyperclip.paste()
    return clipboard_content

if __name__ == '__main__':
    last_clipboard_content = None

    while True:
        action = 'send'
        if action == 'send':
            clipboard_content = get_clipboard_content()

            if clipboard_content != last_clipboard_content:
                last_clipboard_content = clipboard_content

                message_type = classify_clipboard_content(clipboard_content)
                send_message(clipboard_content, message_type)
        elif action == 'send file':
            file_path = input('Enter the file path: ')
            send_file(file_path)
        elif action == 'get':
            get_messages()
        else:
            print('Invalid input. Please try again.')
        
        time.sleep(0.1)
