def load_constitution():
    f = open("constitution.txt", "r")
    lines = f.readlines()
    f.close()

    # remove spaces and newline characters from each line
    clean_lines = []
    for line in lines:
        clean_lines.append(line.strip())

    return clean_lines


def find_sections(lines, term):
    term = term.lower()
    sections = [] 
    i = 0

    while i < len(lines):
        if term in lines[i].lower():
            # find the start of this section (goes up until a blank line)
            start = i
            while start > 0 and lines[start - 1] != "":
                start = start - 1

            #find the end of this section (goes down until a blank line)
            end = i
            while end < len(lines) - 1 and lines[end + 1] != "":
                end = end + 1
            sections.append((start, end))

            # skip to the next section
            i = end + 1
        else:
            i = i + 1

    return sections


def print_section(lines, start, end):
    #print all lines between start and end (inclusive)
    for i in range(start, end + 1):
        print("Line", i + 1, ":", lines[i])
    print()  # blank line after each section


def main():
    #loads the constitution
    lines = load_constitution()

    #lets the user search repeatedly
    while True:
        term = input("Enter search term (or press Enter to quit): ").strip()

        if term == "":
            print("Exiting program.")
            break
        found_sections = find_sections(lines, term)
        if len(found_sections) == 0:
            print("No matches found.\n")
        else:
            for start, end in found_sections:
                print_section(lines, start, end)

main()