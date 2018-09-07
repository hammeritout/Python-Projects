"""
Program: cube.py
Author: Sharyl Hammer
Date: September 11, 2017

The purpose of this program is to calculate the surface area of a cube.
The input is an integer representing the length of the cube. The output
prints the surface area of the cube.

1. The input is
   length of the cube

2. Computations:
   surface_area  = length ** 2 * 6

   Example: length is 15, (15 * 15)  = 125 *6 = 1350
   A cube a six sides.
   """
length = int(input("Enter the length of the cube: "))

#Compute the surface area

surface_area = length ** 2 * 6

print("The surface area is " + str(int(surface_area)))


      
