pcards = ['0-Y','1-R','2-B','3-G','+2-B']
test = []
dict = {
'0':[],
'1':[],
'2':[],
'3':[],
'4':[],
'5':[],
'6':[],
'7':[],
'8':[],
'9':[],
'+2':[],
'+4':[],
'W-':[],
'S-':[],
'R-':[],
}
print(dict['0'])
for i in pcards:   
    a = i.split('-')
    for j in dict.keys():
        if a[i]==dict.keys(j):
            dict[j[i]]
print(dict)
    
    
