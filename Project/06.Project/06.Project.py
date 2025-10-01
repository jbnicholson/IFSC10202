input_file = "06.Project Input File.txt"
merge_file = "06.Project Merge File.txt"
output_file = "06.Project Output File.txt"

# counters
input_count = 0
merge_count = 0
output_count = 0

with open(input_file, "r") as fin, open(output_file, "w") as fout:
    for line in fin:
        input_count += 1
        if "**Insert Merge File Here**" in line:
            with open(merge_file, "r") as fmerge:
                for mline in fmerge:
                    fout.write(mline)
                    merge_count += 1
                    output_count += 1
        else:
            fout.write(line)
            output_count += 1

print(f"{input_count} input file records")
print(f"{merge_count} merge file records")
print(f"{output_count} output file records")