def display(lines,start,end):
    print("\n")
    for i in range(start, end + 1):
        print(f"Line{i + 1}: {lines[i]}")
    print("\n")

def main():
    file = open("constitution.txt", "r" )
    lines = []
    for line in file:
        lines.append(line.strip())
        file.close()

search_term = input("Enter search term: ").strip()

while search_term != "":
    