print("First Timestamp")
x = int(input("Hours: "))
x *= 1440
y = int(input("Minutes: "))
y *= 60
z = int(input("Seconds: "))

print("Second Timestamp")
a = int(input("Hours: "))
a *= 1440
b = int(input("Minutes: "))
b *= 60
c = int(input("Seconds: "))

print(a-x + b-y + c-z)

