with open("09.Project Distances.csv") as file:
    lines = file.readlines()

#2D list
table = []
for line in lines:
    parts = line.strip().split(",")
    table.append(parts)

# print the table neatly
for row in table:
    for item in row:
        print(f"{item:>12}", end="")
    print()
print("\n")

#ask for cities
from_city = input("Enter From City: ").strip()
to_city = input("Enter To City: ").strip()

from_index = -1
to_index = -1

# find From City 
for i in range(1, len(table)):
    if table[i][0].lower() == from_city.lower():
        from_index = i
        break

# find To City
for j in range(1, len(table[0])):
    if table[0][j].lower() == to_city.lower():
        to_index = j
        break

if from_index == -1:
    print("Invalid From City")
elif to_index == -1:
    print("Invalid To City")
else:
    distance = table[from_index][to_index]
    print(f"{from_city} to {to_city} - {distance} miles")