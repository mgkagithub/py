import json
def read_file():
    with open("C:\\Users\\omega\\OneDrive\\Desktop\\py\\py\\discord_bots\\fueled_bot\\cmds.json", "r") as file:
        data = json.load(file)
        if data == None or data == 0 or data == {}:
            return False
        else:
            return data

def write_file(data):
    with open("C:\\Users\\omega\\OneDrive\\Desktop\\py\\py\\discord_bots\\fueled_bot\\cmds.json", "w") as file:
        json.dump(data, file, indent=4)