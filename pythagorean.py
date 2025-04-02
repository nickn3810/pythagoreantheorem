# For: Geometry 2D | Creator: Nick N. | Teacher: Matt Donovan
# -------------------------------------------------------

from math import sqrt, pow

a = int(input("A = "))
b = int(input("B = "))

a = pow(a, 2)
b = pow(b, 2)

c = a + b

c = sqrt(c)

print(f"----------------\nC = {c}")
