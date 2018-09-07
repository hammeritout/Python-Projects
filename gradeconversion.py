"""
Program: gradeconversion.py
Author: Sharyl Hammer
Date: October 9, 2017
  
   """

while True:
    number = int(input("Enter the numeric grade: "))
    if number >= 0 and number <= 100:
        break
    else:
        print("Error: grade must be between 100 and 0")
print(number)
        
