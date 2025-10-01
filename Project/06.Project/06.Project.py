input_file = "06.Project Input File.txt"
merge_file = "06.Project Merge File.txt"
output_file = "06.Project Output File.txt"

# counters
input_count = 0
merge_count = 0
output_count = 0

with open(output_file, "w") as output_file:
    with open(input_file, "r") as input_file:
        for line in input_file:
            input_count += 1
        #check for a merge trigger
            if "**Insert Merge File Here**" in line:
                output_file.write(line)
                output_count += 1
                #open the merge file and copy the contents
                with open(merge_file, "r") as merge_file:
                    for merge_line in merge_file:
                        output_file.write(merge_line)
                        merge_count += 1
                        output_count += 1
            else:
                output_file.write(line)
                output_count += 1

input_file.close()
output_file.close()

print(f"{input_count} input file records")
print(f"{merge_count} merge file records")
print(f"{output_count} output file records")