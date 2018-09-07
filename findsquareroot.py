"""
Program: findsquareroot.py
Author: Sharyl Hammer
Date: October 29, 2017

The purpose of this program is to calculate a number's square root.
The input is a number and the program will continue to process a square root
until the enter presses the enter key which the loop is exited when a enter key is
is pressed.

1. The input is
   a number

2. Computations:
   calculates the newton square root. 
   determines the square root of a number using the math function .sqrt

   The program uses a main function which the main function calls the newton
   function and calculates the square root.
   Uses a recursive function controlling loop with the enter key pressed will exit the
   loop.
  
   """
def main():
    import math
    
    """ The main funciton for this script."""
    
    data = input("Please enter a positive number or enter to quit: ")
    while data != " ":
        if not data:
            break
        else:
            number = float(data)
            sum = newton(number)
            print("The calculated newton root is: ", sum)
            print("Python's calculated square root is: ", math.sqrt(number))
            data = input("Please enter a number or just enter to quit: ")

def newton(number):
    
    estimate = 1.0
    tolerance = 0.000001
    while True: 
        estimate = (estimate + number / estimate)/2
        print("This is the estimate:" , estimate)
        difference = abs(number - estimate **2)
        print("This is the difference:", difference)
        if difference <= tolerance:
           return estimate 
 
main()


