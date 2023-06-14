def one():
    print(1,1)
def two():
    print(2,2)
def three():
    print(3,3)
def four():
    print(4,4)
def five():
    print(5,5)
dict1 = {1:'one()',2:'two()',3:'three()',4:'four()',5:'five()'}
def funct1():
    global dict1
    num = int(input("enter num: \n"))
    function_name = dict1[num]
    function_name = function_name.replace("'","")
    print(def function_name)
funct1()