"""
Program: shortcircuit.py
Author: Sharyl Hammer
Date: October 9, 2017
  
   """
count = int(input("Enter the count: "))
sum = int(input("Enter the sum: "))
if count > 0 and sum // count > 10:
    print("average > 10")
else:
    print("count = 0 or average <=10")
    
