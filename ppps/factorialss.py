x = int(input("Enter x:\n"))
n = int(input("Enter n:\n"))
a = 9
sums = 0
def fact(i):
    factorial_a = eval("*".join(str(j) for j in range(1, int(i) + 1)))
    return factorial_a

for i in range(1,n+1):
    b = fact(a)
    a+=4
    sums += b/x
    print(sums)


