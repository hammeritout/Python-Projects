"""
Program: equaltri.py
Author: Sharyl Hammer
Date: October 1, 2017

The purpose of this program is to idenifty if the triangle is equilateral.
The input is three inputs of the length of the sides and bottom of the triangle.

1. The input is
   length of the right, left and bottom side of the triangle

2. Computations:
   Determines if the lengths are equal.

   All sides have to be equal length to be equilateral. 
  
   """
tr_side = int(input("Enter the triangles's right side length:"))
tl_side = int(input("Enter the triangles's left side length:"))
tb_side = int(input("Enter the triangles's bottom side length:"))

#Determine if the triangle is equilateral triangle

if(tr_side == tl_side) and (tr_side == tb_side):
    print("The triangle is an equilateral triangle")

else:    
    print("The triangle is not an equilateral triangle")
        

