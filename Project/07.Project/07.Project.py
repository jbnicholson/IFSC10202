def ParseDegreeString(ddmmss):
    degree_symbol = chr(176)
    deg_pos = ddmmss.find(degree_symbol)
    min_pos = ddmmss.find("'")
    sec_pos = ddmmss.find('"')

    degrees = float(ddmmss[:deg_pos])
    minutes = float(ddmmss[deg_pos+ 1:min_pos])
    seconds = float(ddmmss[min_pos + 1:sec_pos])

    return degrees, minutes, seconds


def DDMMSStoDecimal(degrees, minutes, seconds):
    return degrees + (minutes/ 60) + (seconds / 3600)

inputfile = "07.Project Angles Input.txt"
outputfile = "07.Project Angles Output.txt"
count = 0

ifile = open(inputfile, "r")
ofile = open(outputfile, "w")

for line in ifile:
    line = line.strip()
    
    deg, mins, secs = ParseDegreeString(line)
    deci = DDMMSStoDecimal(deg, mins, secs)
    ofile.write(str(deci) + "\n")
    count += 1

print(f"{count} records processed")



                    