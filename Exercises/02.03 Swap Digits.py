x = int(input("Enter a number: "))

last_digit = x % 10
first_digit = x // 10

swap = last_digit * 10 + first_digit
print(f"Original Number: {x}")
print(f"Swapped Number: {swap}")
