import os
from time import sleep
def tower_of_hanoi(n, source, target, auxiliary):
    if n > 0:
        tower_of_hanoi(n - 1, source, auxiliary, target)
        target.append(source.pop())
        print_towers()
        tower_of_hanoi(n - 1, auxiliary, target, source)
step = -1
def print_towers():
    global step
    os.system('cls')
    print(f"Source Peg: {source_peg}")
    print(f"Target Peg: {target_peg}")
    print(f"Auxiliary Peg: {auxiliary_peg}")
    step+=1
    print(f"Steps - {step}")
n = int(input("Enter the number of discs: "))
source_peg = list(range(n, 0, -1))
target_peg = []
auxiliary_peg = []
print("Initial State:")
print_towers()
tower_of_hanoi(n, source_peg, target_peg, auxiliary_peg)
print("Tower of Hanoi solved!")
print_towers()
