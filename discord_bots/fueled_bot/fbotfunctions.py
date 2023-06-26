import json
def read_file():
    with open("C:\\Users\\omega\\OneDrive\\Desktop\\py\\py\\discord_bots\\fueled_bot\\cmds.json", "r") as file:
        data = json.load(file)
        if data == None or data == 0 or data == {}:
            return data
        else:
            return data

def write_file(data):
    with open("C:\\Users\\omega\\OneDrive\\Desktop\\py\\py\\discord_bots\\fueled_bot\\cmds.json", "w") as file:
        json.dump(data, file, indent=4)

def lock_status():
    with open("C:\\Users\\omega\\OneDrive\\Desktop\\py\\py\\discord_bots\\fueled_bot\\lockunlock.txt", "r") as file:
        status = file.read(8)
        status = status.rstrip()
        return status

def write_lock_status(status):
    with open("C:\\Users\\omega\\OneDrive\\Desktop\\py\\py\\discord_bots\\fueled_bot\\lockunlock.txt", "w") as file:
        if status.lower()=='lock':
            file.write('locked')
            return True
        elif status.lower()=='unlock':
            file.write('unlocked')
            return True
        else:
            return None
