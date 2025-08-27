N = int(input("How many apples are in the basket?: "))
K = int(input("How many students are there?: "))

print("Each student gets", N//K, "apples.")
print("There are", N % K, "apples left in the basket." )