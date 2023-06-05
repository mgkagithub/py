import csv
filename ="C:\\Users\\omega\\OneDrive\\Desktop\\py\\py\\discord_bots\\fueled_bot\\cmds.csv"
cmd_dict = {}
# opening the file using "with"
# statement
with open(filename, 'r') as data:
  for line in data.readlines():
    num = line.split('-')
    num,val = num[0],num[1]
    for i in val:
        val = val.replace("\n","")
        val = val.replace("'","")
    cmd_dict[num] = val
print(cmd_dict)
while True:
    value = input("Enter the name: \n")
    print(cmd_dict[value])

