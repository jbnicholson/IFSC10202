start = int(input("Enter Start of Range: "))
end = int(input("Enter End of Range: "))

for N in range(start, end + 1):
    count = 0 #placeholder number
    temp = N #temporary number so the orignal number isnt ruined
    while temp > 0: #counts the digits in a number
        count += 1
        temp //= 10
    total = 0
    temp = N
    while temp > 0: #calculates the sum of digits raised to the power of (count)
        digit = temp % 10
        total += digit ** count
        temp //= 10
    if total == N:
        print(N)

# this is sick


