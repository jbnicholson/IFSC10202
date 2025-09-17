import math
total = 0

N = int(input("N number: "))

for i in range(0, N+1):
    total += i ** 3

print(total)