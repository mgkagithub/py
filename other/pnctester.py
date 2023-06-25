# from itertools import combinations
# lst = [] 
# for i in range(1,21):
#     lst.append(i)

# x = list(combinations(lst,1))
# y = list(combinations(lst,2))

# print(x,y)
# print(len(x),len(y))/
from itertools import permutations
p = [0 for k in range(6)]
for k in range(0,3):
        p[k] = 1
print(list(permutations(p)))