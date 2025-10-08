inputfile = "07.Project Angles Input.txt"
outputfile = "07.Project Angles Output.txt"
count = 0

ifile = open(inputfile, "r")
ofile = open(outputfile, "w")

for line in ifile:
    line = line.strip()
    if line:
        degree = chr(176)
        degree_sym = line.find(degree)
        min_sym = line.find("'")
        sec_sym = line.find('"')
        deg = float(line[:degree_sym])
        min = float(line[degree_sym + 1:min_sym])
        sec = float(line[min_sym + 1:sec_sym])

        deci = deg + min /60 +sec / 3600

        ofile.write(str(deci) + "\n")

ifile.close()
ofile.close()
print(str(count)+ "records processed")


                    