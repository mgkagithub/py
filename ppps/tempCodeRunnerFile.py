from itertools import permutations
s1,s2,l,sam=1,int(input()),[1 for _ in range(int(input("Enter N: ")))],0
num=len(l)
while 1:
    z=set(permutations(l,len(l)))
    print(z,len(z))
    sam+=len(z)
    for i in range(s2):
        l.remove(s1)
    l.append(s2)
    if l.count(s1) < s2:
        z=set(permutations(l,len(l)))
        print(z,len(z))
        break
print(sam+len(z))