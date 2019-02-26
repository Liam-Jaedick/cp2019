r = int(input("radius(cm): "))
l = int(input("length(cm): "))

from math import pi
a = r ** 2 * pi
v = a * l
print("Volume of the cylinder(cm^3):",v)
