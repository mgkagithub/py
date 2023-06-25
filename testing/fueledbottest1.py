import json
def read_file():
    with open("C:\\Users\\omega\\OneDrive\\Desktop\\py\\py\\testing\\cmds.json", "r") as file:
        data = json.load(file)
    return data

def read_backup_file():
    with open("C:\\Users\\omega\\OneDrive\\Desktop\\py\\py\\testing\\backupcmds.json", "r") as file:
        backup_data = json.load(file)
    return backup_data

def write_file(data):
    with open("C:\\Users\\omega\\OneDrive\\Desktop\\py\\py\\testing\\cmds.json", "w") as file:
        json.dump(data, file, indent=4)

def display_data(data):
    print("Current data:")
    for index, (tag, value) in enumerate(data.items(), start=1):
        print(f"{index}) {tag}: {value}")

def append_data():
    tag = input("Enter the new tag: ")
    value = input("Enter the value: ")
    data = read_file()
    data[tag] = value
    write_file(data)

def modify_name():
    index = int(input("Enter the index of the tag to modify: "))
    data = read_file()
    tags = list(data.keys())
    if index >= 1 and index <= len(tags):
        tag = tags[index - 1]
        new_tag = input("Enter the new tag: ")
        value = data.pop(tag)
        data[new_tag] = value
        write_file(data)
        print(f"Tag '{tag}' modified successfully.")
    else:
        print("Invalid index.")

def modify_value():
    index = int(input("Enter the index of the tag to modify: "))
    data = read_file()
    tags = list(data.keys())
    if index >= 1 and index <= len(tags):
        tag = tags[index - 1]
        new_value = input("Enter the new value: ")
        data[tag] = new_value
        write_file(data)
        print(f"Value of tag '{tag}' modified successfully.")
    else:
        print("Invalid index.")

def delete_tag():
    index_or_name = input("Enter the index or name of the tag: ")
    data = read_file()
    backup_data = read_backup_file()
    tags = list(data.keys())
    if index_or_name.isdigit():
        index = int(index_or_name)
        if index >= 1 and index <= len(tags) and data[index_or_name] not in backup_data:
            tag = tags[index - 1]
            write_file_backup(data[tag])
            del data[tag]
            write_file(data)
            print(f"Tag '{tag}' deleted successfully.")
        else:
            print("Invalid index.")
    else:
        if index_or_name in tags and index_or_name not in backup_data:
            write_file_backup(data[index_or_name])
            del data[index_or_name]
            write_file(data)
            print(f"Tag '{index_or_name}' deleted successfully.")
        else:
            print("Invalid tag name.")

def delete_all():
    confirm = input("Are you sure you want to delete the whole set? (y/n): ")
    if confirm.lower() == 'y':
        data = read_file()
        write_file_backup(data)
        data.clear()
        write_file(data)
        print("The whole set has been deleted and backed up.")
    else:
        print("Operation canceled.")

def write_file_backup(data):
    with open("C:\\Users\\omega\\OneDrive\\Desktop\\py\\py\\testing\\backupcmds.json", "a") as file:
        json.dump(data, file)
        file.write("\n")

# Menu
while True:
    print("\n\n==== JSON Data Manipulation ====\n\n")
    print("1) Read and display current data")
    print("2) Append a tag and value")
    print("3) Delete a tag")
    print("4) Modify the name of a tag")
    print("5) Modify the value of a tag")
    print("6) Delete the whole set")
    print("0) Exit")

    choice = input("\n\nEnter your choice: ")

    if choice == '1':
        data = read_file()
        display_data(data)
    elif choice == '2':
        append_data()
    elif choice == '3':
        delete_tag()
    elif choice == '4':
        modify_name()
    elif choice == '5':
        modify_value()
    elif choice == '6':
        delete_all()
    elif choice == '0':
        break
    else:
        print("Invalid choice. Please try again.")

print("Program exited.")
