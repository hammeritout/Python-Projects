"""
Program: righttri.py
Author: Sharyl Hammer
Date: October 1, 2017

The purpose of this program is to idenifty if the triangle is a right triangle.
The input is three inputs of the length of the sides and bottom of the triangle.

1. The input is
   length of the right, left and bottom side of the triangle

2. Computations:
   C2= A2 +B2  
   The hypotenuse side is the longer side of the triangle. The hypotenuse length side should
   be the same value as the other two sides sum of the square of each value. 
    
   """
tr_side = int(input("Enter the triangles's right side length:"))
tl_side = int(input("Enter the triangles's left side length:"))
tb_side = int(input("Enter the triangles's bottom side length:"))

# Determine which side is the highest.

if(tr_side) > (tl_side):
   high_val = tr_side
else:
   high_val = tl_side

if(high_val) < (tb_side):
   high_val = tb_side

#print("The high value is",high_val)

    # Find the squared value for the hyponetuse side.

hyp_val = high_val ** 2

#print("The hyponetuse value is" ,hyp_val)
# defining variables for the squared values of the sides.
tr_sq = 0
tl_sq = 0
tb_sq = 0
if(tr_side != high_val):
   tr_sq = tr_side ** 2
   
if(tl_side != high_val):
   tl_sq = tl_side ** 2

if(tb_side != high_val):
   tb_sq = tb_side ** 2
   
# one of these values is equal to high_val and will be 0        
if(hyp_val == tr_sq + tl_sq + tb_sq):
       print("The trianlge is a right triangle")
else:
       print("The triangle is not a right triangle") 
      




        

