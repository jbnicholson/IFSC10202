#prompts user for inputs

first = float(input("Enter First Number: " ))
operator = input("Enter Operator(+,-,*,/): ")

second = float(input("Enter Second Number: "))

'''
 this will make sure the user can only use the
 4 operators
 '''
if operator == "+":
    sum = first + second
    print(f"{first} + {second} = {sum}")
elif operator == "-":
    diff = first - second
    print(f"{first} - {second} = {diff}")
elif operator == "*":
    product = first * second
    print(f"{first} * {second} = {product}")
elif operator == "/":
    div = first / second
    print(f"{first} / {second} = {div}")
else:
    print("Invalid input.")
    
