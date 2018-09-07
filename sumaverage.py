"""
Program: sumaverage.py
Author: Sharyl Hammer
Date: October 9, 2017

The purpose of this program is to find the sum and average of the numbers that
are entered in the program. When the user presses the enter key this indicates that
the user is finished providing the input of numbers.

1. Inputs = Random number user enters.



2. Computations:
   SUM = NUMBER + NUMBER + NUMBER
   AVERAGE = SUM / COUNT

3. OUTPUT = Prints the sum and average of the numbers that are input in the program.   
          
   """
count = 0
average = 0
sum = 0.0

data = input("Enter a number or just enter to quit:")
while data != "":
    number = float(data)
    sum += number
    count += 1
    data = input("Enter a number or just enter to quit:")
average = sum / count
print("The sum is", sum)
print("The average is", average)
