#this code will create a pyramid given a number, which determines its height

N = int(input("Enter maximum height: "))

for i in range(1, N+1):
    print("* " * i)

for i in range(N-1, 0,-1):
    print("* " * i)
