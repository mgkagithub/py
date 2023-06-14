from itertools import combinations
from functools import reduce
from operator import add
lst = []
length = int(input("Enter range of list:\n"))
for i in range(length):
    lst.append(int(input("Enter num:\n")))
key = int(input("Enter num: "))
match_sum = []
for i in range(1,len(lst)):
    x = list(combinations(lst, i))
    for matches in x:
        temp = reduce(add,matches)
        if temp == key:
            match_sum.append(matches)
            match_sum.sort()
for i in range(len(match_sum)):
    print(f"{i+1}> {match_sum[i]}",sep='\n')
min , max = len(match_sum[0]),len(match_sum[0])
max_index , min_index = 0,0
for i in range(1,len(match_sum)):
    if len(match_sum[i]) < min:
        min = len(match_sum[i])
        min_index = i
    elif len(match_sum[i]) > max:
        max = len(match_sum[i])
        max_index = i
    else:
        pass
print(f"\n\nmax is {max_index+1}> {(match_sum[max_index])}\nmin is {min_index+1}> {(match_sum[min_index])}")

