print("even" if (num := int(input("enter number: \n")))%2==0 else "odd") # odd or even
print("prime" if all(int(num) % i != 0 for i in range(2, int(num))) and int(num) > 1 else "not prime") # prime or not
print([fib_series.append(fib_series[-1] + fib_series[-2]) or fib_series[-1] if len(fib_series) >= 2 else fib_series.append(1) or 1 for fib_series in [[0]] for _ in range(int(num))][-int(num):]) # fibonacci till N
print(1 if int(num) == 0 else eval('*'.join(str(i) for i in range(1, int(num) + 1)))) # factorial of a number
print(sum(range(1, int(num) + 1))) # sum of all numbers from 1 to num
print(max(i for i in range(2, int(num)) if int(num) % i == 0) if int(num) > 1 else "No prime factor exists.") # highest factor
print('\n'.join([f"{num} x {i} = {num*i}" for i in range(1, 11)])) # multiplication table of a number
print("Leap year" if (year := int(input("Enter the year: "))) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0 else "Not a leap year") # leap year checker
print(next(base**exponent for base, exponent in [(int(input("Enter the base: ")), int(input("Enter the exponent: ")))])) # exponent of a number
print(*("Armstrong number" if sum(int(digit)**len(str(num)) for digit in str(num)) == num else "Not an Armstrong number" for num in num)) # checks for armstrong number