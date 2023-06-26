from itertools import permutations
s1,s2,l,sam=1,int(input("First step is always 1.\nEnter 2nd step: ")),[1 for _ in range(int(input("Enter total stairs: ")))],0
num=len(l)
while 1:
    z=set(permutations(l,len(l)))
    print(z,'\n',len(z),'\n')
    sam+=len(z)
    for i in range(s2):
        l.remove(s1)
    l.append(s2)
    if l.count(s1) < s2:
        z=set(permutations(l,len(l)))
        print(z,'\n',len(z),'\n')
        break
print(f"The final sum is {sam+len(z)}")