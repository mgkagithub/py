import csv
filename ="C:\\Users\\omega\\OneDrive\\Desktop\\py\\py\\discord_bots\\fueled_bot\\cmds.txt"
cmd_dict = {}
# opening the file using "with"
# statement
# with open(filename, 'r') as data:
#   for line in data.readlines():
#     num = line.split('-')
#     num,val = num[0],num[1]
#     for i in val:
#         val = val.replace("\n","")
#         val = val.replace("'","")
#     cmd_dict[num] = val
def add():
  with open(filename, 'a') as data:
    key , value = 'mgg','admin'
    # key = input('add the key name:\n')
    # value = input('add value name:\n')
    value = str(value)
    data_added = key+'-'+value+'\n'
    data.write(data_added)
  print('added')
  return data_added

def del_data():
  with open(filename, 'r+') as data:
    lines = data.readlines()
    # del_key = input("enter tag name to delete: \n")
    print(lines)
    # data.write(key+'-'+value)
  print('deleted')
  # return data_deleted
add()
del_data()
      
    

