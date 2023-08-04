import random
ccards = []
r_ccards = []
s_ccards = []
outcome = []
d = {}

skip_reverse = ['R-R','R-R','S-R','S-R',
                'R-G','R-G','S-G','S-G',
                'R-B','R-B','S-B','S-B',
                'R-Y','R-Y','S-Y','S-Y']

random.shuffle(skip_reverse)
for i in range(random.randint(5,10)):
    ccards.append(skip_reverse[i])
print(ccards)

card = '1-R' #input("Enter top card: \n")

card_config_value = card.split('-')[0]
card_config_color = card.split('-')[1]
a = ccards
# get top card color -> get mode of color -> join one color to another -> join S to R or R to S -> 

while len(a)!=0:
    for i in a:
        if i.startswith('R'):
            r_ccards.append(i)
            a.remove(i)
        elif i.startswith('S'):
            s_ccards.append(i)
            a.remove(i)
        else:
            print('wrong card')
for s in s_ccards:
    if [*s][2]==card_config_color and s_ccards.index(s)!=0:
        print(s_ccards,s,[*s][2],card_config_color)
        s_ccards[s_ccards.index(s)],s_ccards[0] = s_ccards[0],s_ccards[s_ccards.index(s)]
        print(s_ccards)
    else:
        print("card skipped values and references:",s,[*s][2],card_config_color)
for r in r_ccards:
    if [*r][2]==card_config_color and r_ccards.index(r)!=0:
        print(r_ccards,r,[*r][2],card_config_color)
        r_ccards[r_ccards.index(r)],r_ccards[0] = r_ccards[0],r_ccards[r_ccards.index(r)]
        print(r_ccards)
    else:
        print("card skipped values and references:",r,[*r][2],card_config_color)
if r_ccards[0].split('-')[1]==card_config_color:
    for i in range(1,(len(r_ccards))-1):
        for j in s_ccards:
            if r_ccards[i].split('-')[1]==j.split('-')[1]:
                r_ccards[i],r[len[r_ccards]-1],j,s_ccards[0] = r[len[r_ccards]-1],r_ccards[i],s_ccards[0],j
                break
            break
elif s_ccards[0].split('-')[1]==card_config_color:
    for i in range(1,(len(s_ccards))-1):
        for j in r_ccards:
            if s_ccards[i].split('-')[1]==j.split('-')[1]:
                s_ccards[i],s[len[s_ccards]-1],j,r_ccards[0] = s[len[s_ccards]-1],s_ccards[i],r_ccards[0],j
                break
            break
print(r_ccards+s_ccards)


