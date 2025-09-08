from math import pi, sin, cos, acos

print("Great Circle Calculator")

# these will be user inputs

rad = float(input("Enter Radius of the Sphere: "))
x1 = float(input("Starting Point - Enter Latitude: "))
y1 = float(input("Starting Point - Enter Longitude: "))

x2 = float(input("Ending Point - Enter Latitude: "))
y2 = float(input("Ending Point - Enter Longitude: "))

# this will convert the degrees into radians

x1 = x1 * pi / 180
y1 = y1 * pi / 180
x2 = x2 * pi / 180
y2 = y2 * pi / 180

#formula
d = rad * acos(sin(x1) * sin(x2) + cos(x1) * cos(x2) * cos(y1-y2))

#round to nearest hundredths

d = round(d,2)


print(f"The Great Circle Distance is {d}")
