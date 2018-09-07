"""
Program Name: loopbreak.py
Author: Sharyl Hammer
Date: October 9, 2017
"""

sum = 0.0
while True:
    data = input("Enter a number of just enter to quit: ")

    if data == "":
        break
    number = float(data)
    sum += number
    print("The sum is", sum)  
    
    
