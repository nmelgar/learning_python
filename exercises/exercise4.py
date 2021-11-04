#Write a Python program which accepts the radius 
# of a circle from the user and compute the area.
import math

radius = float(input("Enter the radius of the circle:  "))
square_radius = pow(radius, 2)
area = (math.pi * square_radius)

print("The radius of the circle is: " + str(radius))
print("The area of the circle is: " + str(area))