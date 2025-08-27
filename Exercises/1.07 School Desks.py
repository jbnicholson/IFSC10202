# the amount of students in each class
a = int(input("How many students in Class A: "))
b = int(input("How many students in Class B: "))
c = int(input("How many students in Class C: "))

#this code gives the amount of tables needed for each class

a_div = a//2
a_mod = a % 2
a_total = a_div + a_mod

b_div = b//2
b_mod = b % 2
b_total = b_div + b_mod

c_div = c//2
c_mod = c % 2
c_total = c_div + c_mod

total = a_total + b_total + c_total

print(total)

