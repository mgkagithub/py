num = 5
print(f'Highest factor is {max(i for i in range(2, int(num)) if int(num) % i == 0 and len(!=0))}' if int(num) > 1 else "No prime factor exists.")