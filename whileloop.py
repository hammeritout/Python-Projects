"""
Program: whileloop.py
Author: Sharyl Hammer
Date: October 9, 2017
  
   """
sum = 0.0
data = input("Enter a number or just enter to quit:")
while data != "":
    number = float(data)
    sum += number
    data = input("Enter a number or just enter to quit:")
print("The sum is", sum)
